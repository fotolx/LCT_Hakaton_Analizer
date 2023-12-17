from django.http import Http404
from django.shortcuts import render
from .models import PersonResource, Person, Worker
from tablib import Dataset
from django.views.generic import ListView, DetailView
from django.db.models import Max
from django.db.models.functions import Cast
from django.db import models
import json
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


def train_model(request): # for future
    pass

def analize(rows):     
    prediction = calc_probability(rows)
    analized = []
    for i,v in enumerate(rows):
        person = Person.objects.get(pk=v[0])
        person.dismiss=round(float(prediction[i])*100)
        person.save()
        w_id = Worker.objects.get(worker_id=person.worker_id).id
        analized.append({'id':person.id,'w_id':w_id,'worker_id':person.worker_id,'fio':person.fio,'email':person.email,
                         'department':person.department,'period':person.period,'dismiss':person.dismiss})
    return analized

def calc_probability(data_set):
    X=pd.DataFrame(data_set, columns=['id',
            'worker_id',
            'msgs_sent',
            'msgs_recvd',
            'msgs_sent_recipients',
            'msgs_sent_recipients_hidden',
            'msgs_sent_recipients_copy',
            'msgs_late_read',
            'msg_days2read',
            'msg_responded',
            'msgs_sent_length',
            'msgs_sent_afterwork',
            'msgs_sent_rcvd',
            'msgs_sent_rcvd_bytes',
            'msgs_rcvd_question_no_respns'])
    
    with open('regressor_param.txt', 'r') as file:
        json_text=json.load(file)
    model_lr = LinearRegression()
    model_lr.coef_ = np.array(json_text['coef'])
    model_lr.intercept_ = json_text['intercept']

    predicted = model_lr.predict(X.drop(columns=["worker_id","id"]))
    return predicted

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        imported_data = dataset.load(new_persons.read().decode('utf-8'),format='csv')                  
        result = person_resource.import_data(imported_data, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(imported_data, dry_run=False)  # Actually import now
        a=[]
        for row in result.rows:
            if row.import_type=='new' or row.import_type=='update':
                data_row = Person.objects.get(pk=row.object_id).prepare_data()
                a.append(data_row)
        if len(a)>0:
            workers_analized = analize(a)
            return render(request, template_name='analizator.html', 
                    context={'message':True,
                            'analized':True,
                            'skipped':result.totals['skip'],
                            'new':result.totals['new'],
                            'update':result.totals['update'],
                            'error':result.totals['error'],
                            'workers_analized':workers_analized,
                            })
        else:
            return render(request, template_name='analizator.html', 
                    context={'message':True,
                            'analized':False,
                            'skipped':result.totals['skip'],
                            'new':result.totals['new'],
                            'update':result.totals['update'],
                            'error':result.totals['error'],
                            })
    return render(request, template_name='analizator.html', 
                  context={'message':False,'analized':False})

class WorkerList(ListView):
    model = Worker
    context_object_name = 'workers'
    template_name = 'worker_list.html'
    allow_empty = False
    queryset = Worker.objects.order_by('name')
    pass

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['page_header'] = "Все сотрудники"
        context['latest_info'] = dict(Person.objects.filter(pk__in=Person.objects.order_by().values('worker_id').annotate(max_id=Max('id')).values('max_id')).values_list('worker_id','dismiss'))
        context['period_info'] = dict(Person.objects.filter(pk__in=Person.objects.order_by().values('worker_id').annotate(max_id=Max('id')).values('max_id')).values_list('worker_id','period'))
        if len(context['latest_info']) == 0:
            context['no_info'] = True
        else:
            context['no_info'] = False
            context['successful_workers'] = sum(map(lambda x:x<=50, list(context['latest_info'].values())))
            context['bad_workers'] = sum(map(lambda x:x>50, list(context['latest_info'].values())))
        return context
    def get_paginate_by(self, queryset):
        if self.template_name=='person_list.html':
            return 10
        else:
            return 6


class WorkerDetails(DetailView):
    template_name = 'person.html'
    model = Worker
    allow_empty = False

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['worker_data'] = Person.objects.filter(worker_id=self.object.worker_id)
        context['dismiss_history'] = str(list(Person.objects.filter(worker_id=self.object.worker_id).values_list('dismiss', flat=True)))
        context['dismiss_periods'] = (list(Person.objects.filter(worker_id=self.object.worker_id).annotate(dt_as_str=Cast('period', output_field=models.CharField())).values_list('dt_as_str', flat=True)))
        try:
            last = Person.objects.filter(worker_id=self.object.worker_id).order_by('period').latest('period')
        except ObjectDoesNotExist:
            raise Http404
        context['wdata'] = last
        if len(context['worker_data'])>1:
            def calc_percent(what):
                try:
                    return f'{round((last.__dict__[what]-prev.__dict__[what])/prev.__dict__[what]*100):+}%'
                except ZeroDivisionError:
                    return '-'

            prev =Person.objects.filter(worker_id=self.object.worker_id).order_by('-period')[1]
            dict_keys = dict(filter(lambda item: item[0].startswith('msg'),dict.fromkeys(last.__dict__, '').items()))
            for i in dict_keys:
                dict_keys[i] = calc_percent(i)
            
            context['percent'] = dict_keys
        return context
    
def chart_json(request,*args,**kwargs):
    return JsonResponse({'data':str(list(Person.objects.filter(worker_id=Worker.objects.get(id=kwargs['pk']).worker_id).values_list('dismiss', flat=True))),
                         'periods':str(list(Person.objects.filter(worker_id=Worker.objects.get(id=kwargs['pk']).worker_id).annotate(dt_as_str=Cast('period',
                                                                                    output_field=models.CharField())).values_list('dt_as_str', flat=True))),
                         'msgs_sent':str(list(Person.objects.filter(worker_id=Worker.objects.get(id=kwargs['pk']).worker_id).values_list('msgs_sent', flat=True))),})
from django.db import models
from import_export import resources

class Person(models.Model):
    worker_id = models.IntegerField(verbose_name='Табельный номер')
    fio = models.CharField(max_length=50, verbose_name='ФИО')
    email = models.EmailField()
    department = models.CharField(max_length=150, verbose_name='Отдел', blank=True)
    period = models.DateField(verbose_name='Период')
    msgs_sent = models.IntegerField(verbose_name='Количество отправленных сообщений')
    msgs_recvd = models.IntegerField(verbose_name='Количество получаемых сообщений')
    msgs_sent_recipients = models.IntegerField(verbose_name='Количество адресатов в отправляемых сообщениях')
    msgs_sent_recipients_hidden = models.IntegerField(verbose_name='Количество сообщений с адресатами в поле «скрытая копия»')
    msgs_sent_recipients_copy = models.IntegerField(verbose_name='Количество сообщений с адресатами в поле «копия»')
    msgs_late_read = models.IntegerField(verbose_name='Количество сообщений, прочитанных позднее времени получения на 4 часа')
    msg_days2read = models.IntegerField(verbose_name='Количество дней между датой получения и датой прочтения сообщения')
    msg_responded = models.IntegerField(verbose_name='Количество сообщений, на которые произведен ответ')
    msgs_sent_length = models.IntegerField(verbose_name='Количество символов текста в исходящих сообщениях')
    msgs_sent_afterwork = models.IntegerField(verbose_name='Количество сообщений, отправленных вне рамок рабочего дня')
    msgs_sent_rcvd = models.FloatField(verbose_name='Соотношение количества полученных и отправленных сообщений')
    msgs_sent_rcvd_bytes = models.FloatField(verbose_name='Соотношение объема в байтах получаемых и отправляемых сообщений')
    msgs_rcvd_question_no_respns = models.IntegerField(verbose_name='Количество входящих сообщений без ответа, имеющих вопросительные знаки в тексте')
    dismiss = models.FloatField(verbose_name='Вероятность увольнения', default=-1.0)


    def __str__(self) -> str:
            return self.fio+' ('+self.email+') ['+str(self.period)+']'
 
    def prepare_data(self) -> list:
        x = [self.id,
            self.worker_id,
            self.msgs_sent,
            self.msgs_recvd,
            self.msgs_sent_recipients,
            self.msgs_sent_recipients_hidden,
            self.msgs_sent_recipients_copy,
            self.msgs_late_read,
            self.msg_days2read,
            self.msg_responded,
            self.msgs_sent_length,
            self.msgs_sent_afterwork,
            self.msgs_sent_rcvd,
            self.msgs_sent_rcvd_bytes,
            self.msgs_rcvd_question_no_respns]
        return x

class PersonResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        worker_id = row["worker_id"]
        worker_name = row["fio"]
        worker_email = row["email"]
        worker_department = row["department"]
        Worker.objects.get_or_create(worker_id=worker_id, name=worker_name, email=worker_email, department=worker_department,
                                     defaults={"worker_id": worker_id,"name": worker_name, "email": worker_email, "department": worker_department})

    def skip_row(self, instance, original, row, import_validation_errors=None):
        if Person.objects.filter(worker_id=row["worker_id"], period=row["period"]).count()>0:
            return True
        else:
            return False
    
    class Meta:
        model = Person

class Worker(models.Model):
    worker_id = models.IntegerField(verbose_name='Табельный номер')
    name = models.CharField(max_length=50, verbose_name='ФИО')
    email = models.EmailField()
    department = models.CharField(max_length=150, verbose_name='Отдел', blank=True)

    def __str__(self) -> str:
        return self.name+'('+self.email+') ['+self.department+']'      
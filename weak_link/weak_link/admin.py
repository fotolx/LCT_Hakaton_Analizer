from django.contrib import admin
from .models import Person, Worker #, PersonResource
# Register your models here.
admin.site.register(Person)
admin.site.register(Worker)
# admin.site.register(PersonResource)
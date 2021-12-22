from django.contrib import admin
from django.db.models import query

from .models import Choice, Question

admin.site.register(Question)
admin.site.register(Choice)
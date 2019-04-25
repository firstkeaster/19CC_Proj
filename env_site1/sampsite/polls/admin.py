from django.contrib import admin

from .models import Question

## by registering Questions, it appears in POLLS of admin page.
admin.site.register(Question)
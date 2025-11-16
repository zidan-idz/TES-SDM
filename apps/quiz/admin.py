from django.contrib import admin
from .models import Quiz, Question, Result


# MENDAFTAKAN MODEL KE HALAMAN ADMIN
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Result)
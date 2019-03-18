from django.contrib import admin

# Register your models here.

from .models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)


class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')




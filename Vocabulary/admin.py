from django.contrib import admin
from Vocabulary.models import *
# Register your models here.

class WordAdmin(admin.ModelAdmin):
    list_display = ["word_vocab", "category", "exam", "audio"]
    class Meta:
        model = Word

class Quiz_QuestionAdmin(admin.ModelAdmin):
    list_display = ["quiz", "q_type", "text", "correct"]
    class Meta:
        model = Quiz_Question

admin.site.register(Word, WordAdmin)
admin.site.register(Answer_Options)
admin.site.register(Quiz)
admin.site.register(Quiz_Question, Quiz_QuestionAdmin)
from django.db import models
from django.core.files.base import ContentFile
from django.core.files import File
from gtts import gTTS
from tempfile import TemporaryFile
import os
# Create your models here.
class Word(models.Model):
    word_vocab = models.CharField(max_length=200)
    meaning = models.CharField(max_length=300)
    image_url = models.ImageField(upload_to='word_pics/')
    CATEGORY_CHOICES = (
        ('COMMON', 'COMMON'),
        ('EASY', 'EASY'),
        ('MEDIUM', 'MEDIUM'),
        ('MEDIUM 2', 'MEDIUM 2'),
        ('MEDIUM 3', 'MEDIUM 3'),
        ('MEDIUM 4', 'MEDIUM 4'),
        ('HARD', 'HARD'),
        ('HARD 2', 'HARD 2'),
        ('HARD 3', 'HARD 3'),
        ('HARD 4', 'HARD 4'),
    )
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='HARD')
    example = models.CharField(max_length=300, default="____________")
    audio = models.FileField(upload_to='audio/', blank=True)
    EXAM_CHOICES = (
        ('COMMON', 'COMMON'),
        ('GRE', 'GRE'),
        ('GMAT', 'GMAT'),
        ('IELTS', 'IELTS'),
        ('TOEFL', 'TOEFL'),      
    )
    exam = models.CharField(max_length=10, choices=EXAM_CHOICES, default='COMMON')
    

    def save(self, *args, **kwargs):
        audio = gTTS(text=self.word_vocab, lang='en', slow=True)
        audio.save(self.word_vocab + '.mp3')
        f = open(self.word_vocab + '.mp3', 'rb')
        myfile = File(f)
        self.audio = myfile
        super(Word, self).save(*args, **kwargs)

        
    def __str__(self):
        return self.word_vocab

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"



class Answer_Options(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Answer Option"
        verbose_name_plural = "Answer Options"



class Quiz(models.Model):
    quiz_name = models.CharField(max_length=200)

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizes"


class Quiz_Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, default=None, null=True)
    QUESTION_CHOICES = (
        ('FILL_IN_THE_BLANK', 'FILL_IN_THE_BLANK'),
        ('SELECT_BEST_MATCH', 'SELECT_BEST_MATCH'),
    )
    q_type = models.CharField(max_length=30, choices=QUESTION_CHOICES)
    text = models.CharField(max_length=200)
    possible_answers = models.ManyToManyField(Answer_Options)
    selected = models.ForeignKey(Answer_Options, related_name="selected", default=None, on_delete=models.CASCADE, blank=True, null=True)
    correct = models.ForeignKey(Answer_Options, related_name="correct", default=None, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Quiz Question"
        verbose_name_plural = "Quiz Questions"
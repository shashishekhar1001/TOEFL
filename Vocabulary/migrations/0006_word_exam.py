# Generated by Django 2.0.4 on 2018-04-25 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vocabulary', '0005_word_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='exam',
            field=models.CharField(choices=[('COMMON', 'COMMON'), ('GRE', 'GRE'), ('GMAT', 'GMAT'), ('IELTS', 'IELTS'), ('TOEFL', 'TOEFL')], default='COMMON', max_length=10),
        ),
    ]

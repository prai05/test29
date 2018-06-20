# Generated by Django 2.0.6 on 2018-06-20 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_question_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='created',
        ),
        migrations.AlterField(
            model_name='choice',
            name='corrected',
            field=models.BooleanField(choices=[(True, 'True'), (False, 'False')]),
        ),
    ]

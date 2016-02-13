# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 06:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0002_auto_20160210_0514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='description',
            new_name='instruction',
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_type',
            field=models.IntegerField(choices=[(1, 'Fact'), (2, 'Opinion')], default=1),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=250, null=True),
        ),
    ]

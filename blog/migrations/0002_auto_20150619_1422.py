# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='Guest', max_length=30),
        ),
    ]

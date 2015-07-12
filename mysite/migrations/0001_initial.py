# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='visitor_tracking',
            fields=[
                ('ip', models.CharField(serialize=False, primary_key=True, max_length=256)),
                ('recent', models.DateTimeField()),
            ],
        ),
    ]

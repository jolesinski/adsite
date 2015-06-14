# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=4095)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('expire_date', models.DateTimeField(verbose_name=b'expiration date')),
                ('location', models.CharField(max_length=64)),
            ],
        ),
    ]

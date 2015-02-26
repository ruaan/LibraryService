# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=b'255', db_index=True)),
                ('motivation', models.TextField(help_text=b'A motivation for why this book would be a good addition to the library')),
                ('description', models.TextField(help_text=b'A description of what this book is about')),
                ('purchase_url', models.URLField(help_text=b'The url, including http:// where we can purchase this book from')),
                ('price', models.PositiveIntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookRegistry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(default=b'Requested', max_length=20, db_index=True, choices=[(b'Requested', b'Requested'), (b'Approved', b'Approved'), (b'Ordered', b'Ordered'), (b'Available', b'Available'), (b'Out', b'Out'), (b'Overdue', b'Overdue')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(to='api.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

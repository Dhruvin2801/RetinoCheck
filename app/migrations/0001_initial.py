# Generated by Django 2.1.15 on 2020-08-04 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='user-submitted')),
                ('author', models.CharField(default='admin', max_length=255, null=True)),
                ('pred_class', models.CharField(max_length=10)),
                ('preds', models.CharField(max_length=255, null=True)),
                ('uploaded_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]

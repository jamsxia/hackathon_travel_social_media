# Generated by Django 4.2.5 on 2023-09-16 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisitedPlace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitedplace',
            name='visit_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VisitedPlace', '0003_remove_visitedplace_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitedplace',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.2 on 2023-09-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_budget_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='frecuency',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='expense',
            name='type',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Frecuency',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]

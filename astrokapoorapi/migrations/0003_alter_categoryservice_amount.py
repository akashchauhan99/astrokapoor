# Generated by Django 3.2.4 on 2021-06-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrokapoorapi', '0002_categoryservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryservice',
            name='Amount',
            field=models.FloatField(),
        ),
    ]

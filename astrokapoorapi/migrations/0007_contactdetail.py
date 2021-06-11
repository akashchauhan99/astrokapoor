# Generated by Django 3.2.4 on 2021-06-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrokapoorapi', '0006_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(default='', max_length=200)),
                ('Mobile', models.CharField(default='', max_length=20)),
                ('Address', models.TextField()),
                ('Question', models.TextField()),
            ],
        ),
    ]

# Generated by Django 2.0.2 on 2018-04-06 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

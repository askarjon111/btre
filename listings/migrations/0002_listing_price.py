# Generated by Django 3.1.5 on 2021-01-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

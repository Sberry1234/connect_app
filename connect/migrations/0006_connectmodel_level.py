# Generated by Django 3.2.8 on 2021-11-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0005_auto_20211105_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectmodel',
            name='level',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name=''),
        ),
    ]

# Generated by Django 3.2.6 on 2021-11-16 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LPR', '0015_auto_20211115_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorenterdatetime',
            name='exitDateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

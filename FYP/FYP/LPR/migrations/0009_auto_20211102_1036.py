# Generated by Django 3.2.6 on 2021-11-02 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LPR', '0008_endpoint_mlalgorithm_mlalgorithmstatus_mlrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mlalgorithm',
            name='parent_endpoint',
        ),
        migrations.RemoveField(
            model_name='mlalgorithmstatus',
            name='parent_mlalgorithm',
        ),
        migrations.RemoveField(
            model_name='mlrequest',
            name='parent_mlalgorithm',
        ),
        migrations.DeleteModel(
            name='Endpoint',
        ),
        migrations.DeleteModel(
            name='MLAlgorithm',
        ),
        migrations.DeleteModel(
            name='MLAlgorithmStatus',
        ),
        migrations.DeleteModel(
            name='MLRequest',
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-28 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter owner's name (e.g. Tan Soon Lee)", max_length=100)),
                ('unit', models.CharField(help_text="Enter owner's unit number (e.g. 2-12-1)", max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter visitor's name (e.g. Tan Ah Lee)", max_length=100)),
                ('visitUnit', models.CharField(help_text='Enter visited unit (e.g. 2-14-2)', max_length=10)),
                ('visitorPlateNum', models.CharField(help_text="Enter visitor vehicle's license plate number (e.g. PPP1234)", max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(help_text="Enter vehicle's brand (e.g. Honda)", max_length=50)),
                ('model', models.CharField(help_text="Enter vehicle's model (e.g. Civic)", max_length=50)),
                ('colour', models.CharField(help_text='Enter vehicle colour (e.g. Blue)', max_length=20)),
                ('plateNum', models.CharField(help_text='Enter license plate number (e.g. PPP1234)', max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LPR.owner')),
            ],
        ),
    ]

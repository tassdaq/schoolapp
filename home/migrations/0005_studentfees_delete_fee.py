# Generated by Django 4.1 on 2022-11-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_admissionform_id_alter_admissionform_rollid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentfees',
            fields=[
                ('rollid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('fees', models.CharField(max_length=100)),
                ('selectclass', models.CharField(default='Master', max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='fee',
        ),
    ]

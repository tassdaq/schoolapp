# Generated by Django 4.1 on 2022-11-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_admissionform_delete_matric'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admissionform',
            name='id',
        ),
        migrations.AlterField(
            model_name='admissionform',
            name='rollid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 4.1.4 on 2023-01-29 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cnab_file", "0002_alter_cnabfile_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cnabfile",
            name="data",
        ),
    ]

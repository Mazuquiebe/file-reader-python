# Generated by Django 4.1.4 on 2023-01-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cnab_file", "0004_alter_cnabdata_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cnabdata",
            name="value",
            field=models.CharField(max_length=20),
        ),
    ]
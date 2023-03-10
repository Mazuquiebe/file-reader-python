# Generated by Django 4.1.5 on 2023-01-29 06:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CNABData",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("type", models.CharField(max_length=127)),
                ("date", models.DateTimeField(max_length=8)),
                ("value", models.DecimalField(decimal_places=2, max_digits=20)),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=12)),
                ("owner", models.CharField(max_length=6)),
                ("store", models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name="CNABFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="")),
                (
                    "data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cnab_file.cnabdata",
                    ),
                ),
            ],
        ),
    ]

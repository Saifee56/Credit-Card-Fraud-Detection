# Generated by Django 4.2.9 on 2024-04-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("myapp", "0002_delete_transaction"),
    ]

    operations = [
        migrations.CreateModel(
            name="TemporaryFiles",
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
                ("file", models.FileField(upload_to="files/")),
            ],
            options={
                "verbose_name": "Temporary File",
            },
        ),
    ]

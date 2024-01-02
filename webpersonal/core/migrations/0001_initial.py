# Generated by Django 4.2.4 on 2023-10-10 00:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=200)),
                ("descripcion", models.TextField()),
                ("image", models.ImageField(upload_to="project/")),
                ("link", models.URLField(blank=True)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

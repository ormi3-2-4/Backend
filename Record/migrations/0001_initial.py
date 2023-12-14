# Generated by Django 5.0 on 2023-12-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_update", models.DateTimeField(auto_now=True)),
                ("finished_at", models.DateTimeField(blank=True, null=True)),
                (
                    "static_map",
                    models.ImageField(upload_to="record/static_map/%Y/%m/%d/"),
                ),
                ("data", models.TextField(help_text="GPS데이터")),
                ("distance", models.FloatField(help_text="운동한 거리")),
                ("speed", models.FloatField(help_text="평균 속력")),
                ("kind", models.CharField(help_text="운동 종류", max_length=50)),
            ],
            options={
                "verbose_name": "운동 기록",
            },
        ),
    ]

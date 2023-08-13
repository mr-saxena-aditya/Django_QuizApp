# Generated by Django 4.2.4 on 2023-08-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
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
                ("question_text", models.CharField(max_length=200)),
                ("choice1", models.CharField(max_length=100)),
                ("choice2", models.CharField(max_length=100)),
                ("choice3", models.CharField(max_length=100)),
                ("choice4", models.CharField(max_length=100)),
                (
                    "correct_choice",
                    models.PositiveIntegerField(
                        choices=[
                            (1, "Choice 1"),
                            (2, "Choice 2"),
                            (3, "Choice 3"),
                            (4, "Choice 4"),
                        ]
                    ),
                ),
            ],
        ),
    ]

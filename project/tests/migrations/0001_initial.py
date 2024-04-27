# Generated by Django 4.2.9 on 2024-04-26 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
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
                (
                    "name",
                    models.CharField(
                        help_text="напишите название",
                        max_length=150,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
            ],
            options={
                "verbose_name": "тест",
                "verbose_name_plural": "тесты",
            },
        ),
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
                (
                    "text",
                    models.CharField(
                        max_length=100, verbose_name="текст вопроса"
                    ),
                ),
                (
                    "number",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="number"
                    ),
                ),
                (
                    "test",
                    models.ForeignKey(
                        help_text="выберите тест",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        related_query_name="questions",
                        to="tests.test",
                        verbose_name="тест",
                    ),
                ),
            ],
            options={
                "verbose_name": "вопрос",
                "verbose_name_plural": "вопросы",
            },
        ),
        migrations.CreateModel(
            name="Answer",
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
                (
                    "text",
                    models.CharField(
                        max_length=100, verbose_name="текст ответа"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        help_text="выберите вопрос",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        related_query_name="answers",
                        to="tests.question",
                        verbose_name="вопрос",
                    ),
                ),
            ],
            options={
                "verbose_name": "ответ",
                "verbose_name_plural": "ответы",
            },
        ),
        migrations.CreateModel(
            name="AnswerUser",
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
                (
                    "answer",
                    models.ForeignKey(
                        help_text="ответ пользователя",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answerusers",
                        related_query_name="answerusers",
                        to="tests.answer",
                        verbose_name="ответ",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="пользователь",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        related_query_name="answers",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "ответ пользователя",
                "verbose_name_plural": "ответы пользователей",
                "unique_together": {("user", "answer")},
            },
        ),
    ]

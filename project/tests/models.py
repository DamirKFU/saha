import django.db.models

import users.models


__all__ = []


class Test(django.db.models.Model):
    name = django.db.models.CharField(
        "название",
        max_length=150,
        unique=True,
        help_text="напишите название",
    )

    def __str__(self):
        return self.name[:20]

    class Meta:
        verbose_name = "тест"
        verbose_name_plural = "тесты"


class Question(django.db.models.Model):
    test = django.db.models.ForeignKey(
        Test,
        on_delete=django.db.models.CASCADE,
        verbose_name="тест",
        related_name="questions",
        related_query_name="questions",
        help_text="выберите тест",
    )
    text = django.db.models.CharField(
        "текст вопроса",
        max_length=100,
    )
    number = django.db.models.IntegerField(
        blank=True,
        null=True,
        unique=True,
        verbose_name="номер",
        help_text="номер для сортировки вопроса",
    )

    def save(self, *args, **kwargs):
        if not self.number:
            mx_number = Question.objects.filter(
                ~django.db.models.Q(id=self.id),
            ).aggregate(django.db.models.Max(Question.number.field.name))[
                f"{Question.number.field.name}__max"
            ]
            self.number = mx_number + 1 if mx_number else 1

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.text[:30]

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"


class Answer(django.db.models.Model):
    question = django.db.models.ForeignKey(
        Question,
        on_delete=django.db.models.CASCADE,
        verbose_name="вопрос",
        related_name="answers",
        related_query_name="answers",
        help_text="выберите вопрос",
    )

    text = django.db.models.CharField(
        "текст ответа",
        max_length=100,
    )

    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"


class AnswerUser(django.db.models.Model):
    user = django.db.models.ForeignKey(
        users.models.User,
        on_delete=django.db.models.CASCADE,
        verbose_name="пользователь",
        related_name="answers",
        related_query_name="answers",
        help_text="пользователь",
    )
    answer = django.db.models.ForeignKey(
        Answer,
        on_delete=django.db.models.CASCADE,
        verbose_name="ответ",
        related_name="answerusers",
        related_query_name="answerusers",
        help_text="ответ пользователя",
    )

    class Meta:
        verbose_name = "ответ пользователя"
        verbose_name_plural = "ответы пользователей"
        unique_together = (
            "user",
            "answer",
        )

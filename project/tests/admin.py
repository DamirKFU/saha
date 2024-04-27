from django.contrib import admin

import tests.models


__all__ = []


class QuestionInline(admin.TabularInline):
    exclude = []
    model = tests.models.Question


class AnswerInline(admin.TabularInline):
    exclude = []
    model = tests.models.Answer


@admin.register(tests.models.Test)
class TagAdmin(admin.ModelAdmin):
    list_display = (tests.models.Test.name.field.name,)
    inlines = [
        QuestionInline,
    ]


@admin.register(tests.models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (tests.models.Question.text.field.name,)
    inlines = [
        AnswerInline,
    ]

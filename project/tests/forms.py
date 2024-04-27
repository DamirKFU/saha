import django.forms

__all__ = []


class TestForm(django.forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.questions = questions
        for question in questions:
            field_name = f"question_{question.pk}"
            choices = []
            for answer in question.answers.all():
                choices.append(
                    (
                        answer.pk,
                        answer.text,
                    )
                )

            field = django.forms.ChoiceField(
                label=question.text,
                required=True,
                choices=choices,
                widget=django.forms.RadioSelect,
            )
            self.fields[field_name] = field

import django.shortcuts
import django.urls
import django.views.generic

import tests.forms
import tests.models


__all__ = []


class TestFormView(django.views.generic.FormView):
    template_name = "tests/test.html"
    form_class = tests.forms.TestForm
    model = tests.models.Test
    success_url = django.urls.reverse_lazy("tests:test", args=[1])

    def form_valid(self, form):
        return django.shortcuts.redirect(self.success_url)

    def get_form_kwargs(self):
        test_pk = self.kwargs.get("pk")
        django.shortcuts.get_object_or_404(tests.models.Test, pk=test_pk)

        kwargs = super().get_form_kwargs()
        questions = tests.models.Question.objects.filter(test__pk=test_pk)
        kwargs["questions"] = questions

        return kwargs

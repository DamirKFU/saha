import django.urls

import tests.views

app_name = "tests"

urlpatterns = [
    django.urls.path(
        "test/<int:pk>/",
        tests.views.TestFormView.as_view(),
        name="test",
    ),
]

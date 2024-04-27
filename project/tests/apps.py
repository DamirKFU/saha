from django.apps import AppConfig


__all__ = []


class TestsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tests"
    verbose_name = "Тесты"

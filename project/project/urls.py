import django.conf
import django.conf.urls.static
import django.contrib.admin
import django.contrib.auth.urls
import django.urls

urlpatterns = [
    django.urls.path(
        "tests/",
        django.urls.include(("tests.urls")),
        name="tests",
    ),
    django.urls.path("admin/", django.contrib.admin.site.urls),
    django.urls.path(
        "auth/",
        django.urls.include(django.contrib.auth.urls),
    ),
]

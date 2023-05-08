from django.apps import apps

# make sure the critical apps are installed
def test_isInstalled():
    assert apps.is_installed("django.contrib.auth")
    assert apps.is_installed("django_middleware_global_request")
    assert apps.is_installed("django.contrib.sessions")
    assert apps.is_installed("django.contrib.contenttypes")
    assert apps.is_installed("django.contrib.staticfiles")
    assert apps.is_installed("django.contrib.messages")
    assert apps.is_installed("django.contrib.admin")
    assert apps.is_installed("django_filters")
    assert apps.is_installed('users.apps.UserConfig')
    assert apps.is_installed('google.apps.GoogleConfig')
    assert apps.is_installed('widget_tweaks')
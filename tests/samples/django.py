import os
from snoop import snoop

@snoop()
def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.fake_django_settings'
    import django

    django.setup()
    from django.contrib.contenttypes.models import ContentType
    queryset = ContentType.objects.all()
    lst = [1, 2, 3]


expected_output = """
12:34:56.78 >>> Call to main in File "/path/to_file.py", line 5
12:34:56.78    5 | def main():
12:34:56.78    6 |     os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.fake_django_settings'
12:34:56.78    7 |     import django
12:34:56.78 .......... django = <module 'django' from '/User...packages/django/__init__.py'>
12:34:56.78    9 |     django.setup()
12:34:56.78   10 |     from django.contrib.contenttypes.models import ContentType
12:34:56.78 .......... ContentType = <class 'django.contrib.contenttypes.models.ContentType'>
12:34:56.78   11 |     queryset = ContentType.objects.all()
12:34:56.78 .......... queryset = <QuerySet instance of ContentType at 0xABC>
12:34:56.78   12 |     lst = [1, 2, 3]
12:34:56.78 .......... len(lst) = 3
12:34:56.78 <<< Return value from main: None
"""

from django.core.cache import cache
from django.shortcuts import render
from django.db import connection
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def index(request):
    services = {}
    # postgres
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1 AS counter;")
        assert 1 == cursor.fetchone()[0]
        services['postgres'] = 'OK'
    # redis
    if cache.get('counter') is None:
        cache.set('counter', 1)
    assert 1 == cache.get('counter')
    services['redis'] = 'OK'
    # minio
    file_name = "files/hello.txt"
    if not default_storage.exists(file_name):
        default_storage.save(file_name, ContentFile("Hello, world!")  )
    assert default_storage.exists(file_name)
    print(default_storage.url(file_name))
    services['Minio'] = 'OK'

    return render(request, "index.html", context=dict(services=services))

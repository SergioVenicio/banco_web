import base64
import pytest
from django.core.files.base import ContentFile


@pytest.fixture
def path():
    return 'banco_web/tests'

@pytest.fixture
def image_png(path):
    capa = open(path + '/image.png', 'rb').read()
    b64_img = base64.b64encode(capa)
    return ContentFile(base64.b64decode(b64_img), 'test.png')


@pytest.fixture
def image_jpg(path):
    capa = open(path + '/image.jpg', 'rb').read()
    b64_img = base64.b64encode(capa)
    return ContentFile(base64.b64decode(b64_img), 'test.jpg')

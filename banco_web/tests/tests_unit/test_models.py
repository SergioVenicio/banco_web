import pytest
from banco_web.core import models as core_models


@pytest.mark.django_db(transaction=True)
def test_user():
    user = core_models.User.objects.create_user(
        email='teste@teste.com.br', first_name='teste', last_name='testando',
        cpf='111.111.111-11', password='hisudgisfuygd'
    )
    assert isinstance(user.id, int)


@pytest.mark.django_db(transaction=True)
def test_user_error_len_password():
    with pytest.raises(ValueError):
        core_models.User.objects.create_user(
            email='teste@teste.com.br', first_name='teste', last_name='testando',
            cpf='111.111.111-11', password='his'
        )


@pytest.mark.django_db(transaction=True)
def test_user_without_fields():
    with pytest.raises(ValueError):
        core_models.User.objects.create_user(
            email='', first_name='', last_name='', cpf='', password=''
        )


@pytest.mark.django_db(transaction=True)
def test_user_with_avatar_png(image_png):
    user = core_models.User.objects.create_user(
        email='teste@teste.com.br', first_name='teste', last_name='testando',
        cpf='111.111.111-11', avatar=image_png, password='hisudgisfuygd'
    )
    assert isinstance(user.id, int)
    assert user.avatar
    assert user.delete()


@pytest.mark.django_db(transaction=True)
def test_user_with_avatar_jpg(image_jpg):
    user = core_models.User.objects.create_user(
        email='teste@teste.com.br', first_name='teste', last_name='testando',
        cpf='111.111.111-11', avatar=image_jpg, password='hisudgisfuygd'
    )
    assert isinstance(user.id, int)
    assert user.avatar
    assert user.delete()


@pytest.mark.django_db(transaction=True)
def test_superuser():
    user = core_models.User.objects.create_superuser(
        email='teste@teste.com.br', first_name='teste', last_name='testando',
        cpf='111.111.111-11', password='hisudgisfuygd'
    )
    assert isinstance(user.id, int)
    assert user.delete()


@pytest.mark.django_db(transaction=True)
def test_superuser_error_len_password():
    with pytest.raises(ValueError):
        core_models.User.objects.create_superuser(
            email='teste@teste.com.br', first_name='teste', last_name='testando',
            cpf='111.111.111-11', password='his'
        )


@pytest.mark.django_db(transaction=True)
def test_superuser_without_fields():
    with pytest.raises(ValueError):
        core_models.User.objects.create_superuser(
            email='', first_name='', last_name='', cpf='', password=''
        )


@pytest.mark.django_db(transaction=True)
def test_superuser_with_avatar_jpg(image_jpg):
    user = core_models.User.objects.create_superuser(
        email='teste@teste.com.br', first_name='teste', last_name='testando',
        cpf='111.111.111-11', avatar=image_jpg, password='hisudgisfuygd'
    )
    assert isinstance(user.id, int)
    assert user.avatar
    assert user.delete()


@pytest.mark.django_db(transaction=True)
def test_superuser_with_avatar_png(image_png):
    user = core_models.User.objects.create_superuser(
        email='teste@teste.com.br', first_name='teste', last_name='testando',
        cpf='111.111.111-11', avatar=image_png, password='hisudgisfuygd'
    )
    assert isinstance(user.id, int)
    assert user.avatar
    assert user.delete()

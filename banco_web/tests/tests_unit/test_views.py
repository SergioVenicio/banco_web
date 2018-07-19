def test_home(client):
    response = client.get('/')
    assert response.status_code == 302


def test_home_login_client(client, django_user_model):
    email = 'teste@teste.com'
    password = 'dsjkafhdfjkh'
    django_user_model.objects.create_user(
        email=email, first_name='teste', last_name='testando',
        password=password, cpf='111.111.111-11'
    )
    client.login(email=email, password=password)
    response = client.get('/')
    assert response.status_code == 200

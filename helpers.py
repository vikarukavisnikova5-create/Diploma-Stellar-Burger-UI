import uuid
import requests
from data import API_URL

def generate_user():
    suffix = uuid.uuid4().hex[:8]
    return {
        'email': f'test_{suffix}@yandex.ru',
        'password': f'pass_{suffix}',
        'name': f'User{suffix}',
    }

def register_user(user):
    return requests.post(f'{API_URL}/auth/register', json=user)

def delete_user(token):
    return requests.delete(f'{API_URL}/auth/user', headers={'Authorization': token})
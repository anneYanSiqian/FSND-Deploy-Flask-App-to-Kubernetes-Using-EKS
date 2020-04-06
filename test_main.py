'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'Tr9zWgj006pQAFgO3Qbv5hbejmc8ACaP6A33U5hK'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODczNzYyNDIsIm5iZiI6MTU4NjE2NjY0MiwiZW1haWwiOiJhbm5lLnNxLnlhbkBnbWFpbC5jb20ifQ.XCu4CmGpTNSmCgbtbhyZ_Km413tp4MC19ChqlXh-ub0'
EMAIL = 'anne.sq.yan@gmail.com'
PASSWORD = 'YSQ628qiansiyan'

assert False 

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None

from django.urls import reverse
import pytest
import requests
import django.test.client
import pytest
import django.test.utils
from django.conf import settings


def test_home_page():  # Get the home page
    url = 'http://127.0.0.1:8000/sort_by/0/'
    response = requests.get(url)
    assert response.status_code == 200


def test_1():
    url = 'http://127.0.0.1:8000/?sort=ascending'
    response = requests.get(url)
    assert response.status_code == 200


def test_2():
    url = 'http://127.0.0.1:8000/?sort=descending'
    response = requests.get(url)
    assert response.status_code == 200


def test_7():
    url = 'http://127.0.0.1:8000/cart/'
    response = requests.get(url)
    assert response.status_code == 403


def test_8():
    url = 'http://127.0.0.1:8000/order/create/'
    response = requests.get(url)
    assert response.status_code == 403


def test_9():
    url = 'http://127.0.0.1:8000/statistic/'
    response = requests.get(url)
    assert response.status_code == 403

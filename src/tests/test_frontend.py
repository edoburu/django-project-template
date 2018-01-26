"""Test the frontend code"""
import pytest


@pytest.mark.django_db
def test_healthchecks(client):
    response = client.get('/api/health/')
    assert response.status_code in (200, 503)


@pytest.mark.django_db
def test_error_pages(client):
    response = client.get('/404/')
    assert response.status_code == 404

    response = client.get('/500/')
    assert response.status_code == 500


def test_serve_web_file(client):
    response = client.get('/browserconfig.xml')
    assert response.status_code == 200


@pytest.mark.django_db
def test_sitemap(client):
    response = client.get('/sitemap.xml')
    assert response.status_code == 200


def test_robots(client):
    response = client.get('/robots.txt')
    assert response.status_code == 200

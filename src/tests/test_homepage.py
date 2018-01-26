import pytest

from django.contrib.auth.models import User
from django.test import TestCase
from fluent_contents.tests.factories import create_placeholder, create_content_item
from fluentcms_jumbotron.models import JumbotronItem

from fluent_pages.models import PageLayout
from fluent_pages.pagetypes.fluentpage.models import FluentPage


@pytest.mark.django_db
def test_get_homepage(client):
    # Create the page
    user = User.objects.create(username='unittest')
    layout = PageLayout.objects.create(title='homepage', template_path='pages/homepage.html')
    page = FluentPage.objects.create(slug='homepage', override_url='/', layout=layout, author=user, status=FluentPage.PUBLISHED)

    placeholder = create_placeholder(page, slot='homepage')
    create_content_item(JumbotronItem, placeholder, title="JUMBO_TEST", content="Hello!")

    response = client.get('/')
    assert b'JUMBO_TEST' in response.content

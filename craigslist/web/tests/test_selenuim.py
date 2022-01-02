from datetime import datetime
from time import sleep

from django.test import LiveServerTestCase
from selenium import webdriver

from api_v0.models import User
from api_v0.models import Advertisement
from api_v0.models import Category


class SeleniumTest(LiveServerTestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(username="test_user", password="test_password")
        user.save()

        category = Category.objects.create(category="test_category")
        category.save()

        advertisement = Advertisement.objects.create(
            title="advertisement_title",
            description="advertisement_description",
            price=100000,
            pub_date=datetime.now().date(),
            published=True,
            user=user,
            category=category
        )
        advertisement.save()

        self.client.force_login(user)
        cookie = self.client.cookies['sessionid']

        self.driver = webdriver.Firefox()
        self.driver.get(self.live_server_url + '/web/')
        self.driver.add_cookie({
            'name': 'sessionid',
            'value': cookie.value,
            'secure': False,
            'path': '/'
        })
        self.driver.refresh()

    def tearDown(self) -> None:
        self.driver.close()

    def test_click_on_advertisement(self) -> None:
        self.driver.get(f'{self.live_server_url}/web/')
        sleep(1)

        self.assertTrue("Logout" in self.driver.page_source)
        self.assertTrue("Add new advertisement" in self.driver.page_source)

        for advertisement in Advertisement.objects.all():
            self.assertTrue(advertisement.title in self.driver.page_source)

        link = self.driver.find_element(value=f'adv_{1}', by="id")
        link.click()

        self.assertEqual(self.driver.current_url,
                         f'{self.live_server_url}/web/advertisements/1')

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class SiteTest(StaticLiveServerTestCase):
    def setUp(self):
        self._path = FirefoxBinary('/opt/firefox-dev/firefox/firefox')
        self.browser = webdriver.Firefox(firefox_binary=self._path)

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get(self.live_server_url)

        page_title = 'Banco Web'
        page_title_tag = self.browser.find_element_by_class_name(
            'navbar-brand'
        ).text
        self.assertIn(page_title, page_title_tag)

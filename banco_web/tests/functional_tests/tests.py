import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class SiteTest(StaticLiveServerTestCase):
    def setUp(self):
        self._path = FirefoxBinary('/opt/firefox/firefox')
        self.browser = webdriver.Firefox(firefox_binary=self._path)
        self.password = self._get_random_password()
        self.email = 'teste@testando.com.br'

    def tearDown(self):
        self.browser.quit()

    @staticmethod
    def _get_random_password():
        return ''.join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(10)
        )

    def test_home_page(self):
        self.browser.get(self.live_server_url)

        page_title = 'Banco Web'
        page_title_tag = self.browser.find_element_by_class_name(
            'navbar-brand'
        ).text
        self.assertIn(page_title, page_title_tag)

        btn_sign_up = self.browser.find_element_by_id('btn-sing-up').get_attribute('href')

        self.browser.get(btn_sign_up)

        input_email = self.browser.find_element_by_id('id_email')
        input_email.send_keys(self.email)

        input_first_name = self.browser.find_element_by_id('id_first_name')
        input_first_name.send_keys('Teste')

        input_last_name = self.browser.find_element_by_id('id_last_name')
        input_last_name.send_keys('Testando')

        input_password = self.browser.find_element_by_id('id_password1')
        input_password.send_keys(self.password)

        input_password_confirm = self.browser.find_element_by_id('id_password2')
        input_password_confirm.send_keys(self.password)

        btn_sign_up = self.browser.find_element_by_id('btn-sign-up')
        btn_sign_up.send_keys(Keys.ENTER)
        time.sleep(3)
        url = self.browser.current_url

        self.assertNotIn('/sign_up', url)

        time.sleep(1)

        self.browser.get(self.live_server_url + '/logout')

        logout_msg = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(logout_msg, 'Logout realizado com sucesso!')

        self.browser.get(self.live_server_url)

        input_email = self.browser.find_element_by_id('id_username')
        input_password = self.browser.find_element_by_id('id_password')

        input_email.send_keys(self.email)
        input_password.send_keys(self.password)

        time.sleep(5)

        btn_sign_in = self.browser.find_element_by_id('btn-sign-in')
        btn_sign_in.send_keys(Keys.ENTER)
        time.sleep(3)
        url = self.browser.current_url
        self.assertNotIn('?next=', url)

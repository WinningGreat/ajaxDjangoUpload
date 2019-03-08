from django.test import TestCase, client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common import exceptions
from django.urls import reverse
from uploader.views import Upload_Handler_View
from selenium import webdriver
from ajaxUpload.settings import BASE_DIR
import os
from uploader.models import UploadModel

class test_upload_selenium(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        #the executable_path should be set to the location of your geckodriver.exe
        cls.selenium = webdriver.Firefox(executable_path='C:\geckodriver.exe')
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()


    def test_upload(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/upload/'))
        self.selenium.find_element_by_name("myFile").send_keys(os.path.join(BASE_DIR, "uploader\\tests\\assets\\me.jpg"))
        try:
            self.selenium.find_element_by_id("btn_submit").click()

        except exceptions.UnexpectedAlertPresentException:
            self.assertIn("upload", self.selenium.current_url)




class test_upload_handler_view(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')


    def tearDown(self):
        self.driver.quit()


    def test_view_get_response(self):
        resp = self.client.get("/upload/") or self.client.get("")
        self.assertEqual(resp.status_code,200)

    def test_view_post_response(self):

        resp =self.client.post("/upload/") or self.client.get("")

        self.assertEqual(resp.status_code,(200 or 201))
        self.assertEqual(resp.json()['details'],"Select a file")

    def test_view_post_file(self):

        with open(os.path.join(BASE_DIR,"uploader\\tests\\assets\\me.jpg"),encoding='cp850') as up:
            resp = self.client.post("/upload/",{"myFile":up})

        self.assertEqual(resp.json()["file_names"],["me.jpg"])







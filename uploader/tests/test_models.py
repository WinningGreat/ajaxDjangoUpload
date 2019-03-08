from django.test import TestCase
from uploader.models import UploadModel
from model_mommy import mommy
import os
from ajaxUpload.settings import BASE_DIR
# Create your tests here.



class test_upload_model(TestCase):

    def setUp(self):
        '''self.model_test = UploadModel.objects.create(file='bookApp/tests/assets/me.jpg',file_name="model_upload.epub")'''
        self.model_test = mommy.make(UploadModel)

    def test_instance_and_str(self):

        self.assertIsInstance(self.model_test,UploadModel,msg="Should be an instance of Uploadmodel")
        self.assertEqual(self.model_test.file_name,self.model_test.__str__())

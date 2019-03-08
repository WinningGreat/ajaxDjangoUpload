from django.db import models

# Create your models here.
class UploadModel(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    file_name = models.CharField(max_length=255,blank=False)

    def __str__(self):
        return "{0}".format(self.file_name)
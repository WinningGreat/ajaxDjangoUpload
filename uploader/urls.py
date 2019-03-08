from django.urls import re_path
from uploader.views import Upload_Handler_View


urlpatterns = [
    re_path(r'', Upload_Handler_View.as_view(),name="Upload")
]
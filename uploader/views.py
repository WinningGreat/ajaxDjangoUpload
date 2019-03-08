from django.shortcuts import render
from .models import UploadModel

from django.views import View
from django.http import JsonResponse
# Create your views here.
class Upload_Handler_View(View):


    def post(self,request):
        data = {}
        if 'myFile' in request.FILES:
            self.files = request.FILES.getlist('myFile')
            data["file_names"] = []
            print("number of uploading files is {0}".format(len(self.files)))
            for file in self.files:
                data["file_names"].append(file.name)
                UploadModel.objects.create(file=file,file_name=file.name)
            return JsonResponse(data)

        else:
            data["details"]= "Select a file"
            return JsonResponse(data)


    def get(self,request):

        return render(request, 'uploads.html')
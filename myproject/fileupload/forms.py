from django import forms
from .models import UploadedFile
# /Users/sid/Documents/VE/myproject/fileupload/forms.py

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

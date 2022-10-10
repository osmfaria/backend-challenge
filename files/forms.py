from .validators import validate_file_extension

from django import forms  

class FileForm(forms.Form):  
    file = forms.FileField(validators=[validate_file_extension]) 
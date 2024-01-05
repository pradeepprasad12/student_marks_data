from django import forms
from .models import Student
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'class_level', 'subject1', 'subject1_score', 'subject2', 'subject2_score', 'subject3', 'subject3_score', 'subject4', 'subject4_score', 'subject5', 'subject5_score','image']

        
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            img = Image.open(image)
            width, height = img.size
            if width > 600 or height > 600:
                raise ValidationError("Please upload a passport-sized image (max 600x600 pixels).")
        return image
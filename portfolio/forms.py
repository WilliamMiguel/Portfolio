from django import forms
from portfolio.models import Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# creating a form
class NewProjectForm(forms.ModelForm):
  # image = forms.FileField(label="Imágenes", widget=forms.ClearableFileInput(attrs={
  #   'multiple': True
  # }))
  description = forms.CharField(label="Descripción", widget=forms.Textarea())
  
  class Meta:
    model = Project

    fields = [
      'banner',
      'title',
      'description',
      'tags',
      'github'
    ]

    labels = {
      'banner': 'Foto',
      'title': 'Título',
      'description': 'Descripción',
      'tags': 'Tags',
      'github': 'URL de GitHub'
    }

    widgets = {
      # 'image': forms.FileInput(attrs={'class': 'form-control'}),
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      # 'description': forms.Textarea(attrs={'class': 'form-control'}),
      'tags': forms.TextInput(attrs={'class': 'form-control'}),
      'github': forms.TextInput(attrs={'class': 'form-control'})     
    }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
      model = User
      fields = [
        'username',
        'email',
        'password1',
        'password2'
      ]
      help_texts = {k:"" for k in fields}
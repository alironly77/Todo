from pyexpat import model
from django import forms
from .models import Todo
from django.core.exceptions import ValidationError


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["Title", "Description", "Status_Choices"]

        def clean_title(self):
            title = self.cleaned_data['Titele',
                                      "Description", "Status_Choices"]

            return title


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

# forms.py
from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Add new...'
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'text',
                'class': 'form-control date',
                'id': 'datepicker',  
            }),
        }

from django.forms import ModelForm, TextInput, EmailInput, Textarea

from .models import Comment

class CommentForm(ModelForm):
    class Meta:
         model = Comment
         fields = ['user_name', 'email','text']
         widgets = {
             'user_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя',
                                           'aria-required':'true', 'aria-invalid':'true'}),
             'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите почту',
                                           'aria-required': 'true', 'aria-invalid': 'true'}),
             'text': Textarea(attrs={'rows':'2', 'class': 'text-area-messge form-control',
                                        'placeholder': 'Введите комментарий',
                                           'aria-required': 'true', 'aria-invalid': 'false'})
         }

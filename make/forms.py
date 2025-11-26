from django.forms import ModelForm
from .models import PhotoPost
from django import forms

class PhotoPostForm(ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category', 'title', 
        'comment_1', 'comment_2', 
        'image1', 'image2',
         'video']

#お問い合わせform
class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=100, required=True)
    email = forms.EmailField(label='返信先メール', required=True)
    question_title = forms.CharField(label='件名', max_length=120, required=True)
    question_detail = forms.CharField(label='本文', widget=forms.Textarea, required=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


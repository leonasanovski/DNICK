from django import forms
from myapp.models import Cake


class AddCakeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCakeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Cake
        exclude = ['baker']

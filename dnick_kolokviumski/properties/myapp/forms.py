import form
from django import forms  # vazhen import

from myapp.models import RealEstate


class AddRealEstate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddRealEstate, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = RealEstate
        fields = '__all__'

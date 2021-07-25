from django import forms
from .models import Demo

# class AppointmentForm(forms.ModelForm):

#     class Meta:
#         model = Demo
#         fields = "__all__"

#     date = forms.DateField(
#         widget=forms.DateInput(format='%m/%d/%Y'),
#         input_formats=('%m/%d/%Y', )
#         )

# class DemoForm(forms.ModelForm):
#     date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
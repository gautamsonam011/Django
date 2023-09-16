from SMS.models import *
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
class PaymentDetailsForm(forms.ModelForm):
    class Meta:
        model = PaymentDetails
        fields = '__all__'
    def _init_(self,*args,**kwargs):
        super()._init_(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"]="form-control"
            field.widget.attrs["placeholder"]="Enter "+field.label   
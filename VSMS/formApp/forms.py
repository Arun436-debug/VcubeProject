from django import forms
from adminstaff.models import Students



class Stdform(forms.Form):
    stdno = forms.IntegerField()
    StdName = forms.CharField(max_length=30)
    qualification = forms.CharField(max_length=20)
    email = forms.EmailField()
    DOJ = forms.DateField()
    batch = forms.CharField(max_length=20)
    image = forms.ImageField()
    
    
class Stddata(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'



from rest_framework.serializers import ModelSerializer
from adminstaff.models import Students,Attendence
from formApp.forms import Stddata

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields ='__all__'

class AttendenceSerializer(ModelSerializer):
    class Meta:
        model = Attendence
        fields = '__all__'


class FormSerializer(ModelSerializer):
    class Meta:
        model = Stddata
        fields = '__all__'
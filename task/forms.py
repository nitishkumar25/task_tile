from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title','order','desc','type','assg_user','tile') 
        labels = {
            'desc' : 'Description',
            'assg_user' : 'Assigned User'
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm,self).__init__(*args, **kwargs)
        self.fields['tile'].empty_label = "Select"
        self.fields['desc'].required = False
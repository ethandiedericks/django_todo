from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Enter a task here", "class":"form-control"}))

    class Meta:
        model = Task
        fields = ('title',)
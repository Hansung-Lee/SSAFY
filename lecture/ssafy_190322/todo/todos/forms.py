from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'


# class ScoreForm(forms.ModelForm):
#     class Meta:
#         model = Score
#         fields = '__all__'

from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):
    content = forms.CharField(label = "content", widget=forms.Textarea(attrs={
                'rows' : 1,
                'cols' : 20,
            }))
    class Meta:
        model = Score
        fields = ['content', 'value']
        widget = {
            'content' : forms.Textarea
        }


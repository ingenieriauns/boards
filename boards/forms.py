from  django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'Que tienes en mente?'}
        ),
        max_length=4000,
        help_text='El máximo de caracteres es 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
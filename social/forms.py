from django import forms

from .models import Discussions, Comment
from mptt.forms import TreeNodeChoiceField

from tinymce.widgets import TinyMCE

class AddDiscussionForm(forms.ModelForm):

    class Meta:
        model = Discussions
        fields = ['title', 'description', 'status']

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})

        self.fields['description'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})


class CreateCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update({'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ['body', 'parent']
        widgets = {
            forms.TextInput(attrs={'placeholder': 'Добавить комментарий'})
        }
        labels = {
            'body': ''
        }

class SearchForm(forms.Form):
    query = forms.CharField()
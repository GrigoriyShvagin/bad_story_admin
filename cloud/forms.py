from django import forms

from .models import Folder, File


class CreateFolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']


class DeleteFolderForm(forms.Form):
    folders = forms.ModelMultipleChoiceField(
        queryset=Folder.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Выберите папки'
    )


class AddFile(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']
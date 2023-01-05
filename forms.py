from django import forms
from .models import Post

class FormClass(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    class Meta:
        model = Post
        fields = ('project', 'description', 'category', 'team', 'pm', 'second_menber', 'third_menber', 'url')
        labels = {'project':'プロジェクト名', 'description':'概要', 'category':'セメスター', 'team':'チーム名', 'pm':'PM', 'second_menber':'メンバー１', 'third_menber':'メンバー２', 'url':'URL'}
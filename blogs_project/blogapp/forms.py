from . models import Blogs
from django import forms
class Blogforms(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=['heading','desc','content','date']
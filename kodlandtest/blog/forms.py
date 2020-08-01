from django import forms
from .models import Post
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
	class Meta:
		model 	= Post
		fields	= ('title', 'content', 'image')

		widgets 	= {
			'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title'}),
			'image': forms.FileInput(attrs={'class':'form-control'}),
			'content': RichTextField(blank=True,null=True),
		}
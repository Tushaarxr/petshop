from django.forms import ModelForm

from .models import Post, PostAttachment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'contact_information', 'price', 'category', 'body',]


class AttachmentForm(ModelForm):
    class Meta:
        model = PostAttachment
        fields = ('image',)
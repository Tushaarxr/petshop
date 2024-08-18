from django.forms import ModelForm

from .models import Post, PostAttachment,Event,EventAttachment


# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'description', 'contact_information', 'price', 'category', 'body']
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 
            'description', 
            'contact_information', 
            'price', 
            'category', 
            'breed', 
            'color', 
            'age', 
            'vaccinated', 
            'gender', 
            'weight', 
            'microchipped', 
            'trained', 
            'health_certificate', 
            'body'
        ]


class AttachmentForm(ModelForm):
    class Meta:
        model = PostAttachment
        fields = ('image',)
        
        
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']    
        
class EventAttachmentForm(ModelForm):
    class Meta:
        model = EventAttachment
        fields = ['image']            
        
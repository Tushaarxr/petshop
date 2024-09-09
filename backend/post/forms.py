from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Post, PostAttachment, Event, EventAttachment


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
        help_texts = {
            'age': 'Age in months',
            'weight': 'Weight in kilograms',
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Price must be a positive number.")
        return price

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age < 0:
            raise ValidationError("Age cannot be negative.")
        return age

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight <= 0:
            raise ValidationError("Weight must be a positive number.")
        return weight


class AttachmentForm(ModelForm):
    class Meta:
        model = PostAttachment
        fields = ('image',)

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # Limit file size to 5MB
                raise ValidationError("Image file too large ( > 5MB ).")
        return image


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']    


class EventAttachmentForm(ModelForm):
    class Meta:
        model = EventAttachment
        fields = ['image']  

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # Limit file size to 5MB
                raise ValidationError("Image file too large ( > 5MB ).")
        return image

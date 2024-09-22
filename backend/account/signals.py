from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post, User

# Signal to update posts_count when a post is created
@receiver(post_save, sender=Post)
def update_posts_count_on_create(sender, instance, created, **kwargs):
    if created:
        user = instance.created_by  # Assuming you have a ForeignKey to the user
        user.posts_count = user.post_set.count()  # Updates count
        user.save()

# Signal to update posts_count when a post is deleted
@receiver(post_delete, sender=Post)
def update_posts_count_on_delete(sender, instance, **kwargs):
    user = instance.created_by
    user.posts_count = user.post_set.count()
    user.save()

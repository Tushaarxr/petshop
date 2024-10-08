# Generated by Django 5.0.6 on 2024-08-28 19:46

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_eventattachment_event_attachments'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='post.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'unique_together': {('post', 'user')},
            },
        ),
    ]

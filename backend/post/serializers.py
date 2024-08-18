from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Post, PostAttachment, Comment, Trend, Event,EventAttachment


class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = (
            "id",
            "get_image",
        )


# class PostSerializer(serializers.ModelSerializer):
#     created_by = UserSerializer(read_only=True)
#     attachments = PostAttachmentSerializer(read_only=True, many=True)

#     class Meta:
#         model = Post
#         fields = ('id','title', 'description', 'contact_information', 'price', 'category', 'body', 'likes_count', 'comments_count', 'created_by', 'created_at_formatted', 'attachments')

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = (
            'id', 
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
            'body', 
            'likes_count', 
            'comments_count', 
            'created_by', 
            'created_at_formatted', 
            'attachments'
        )



class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "id",
            "body",
            "created_by",
            "created_at_formatted",
        )


class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "body",
            "likes_count",
            "comments_count",
            "created_by",
            "created_at_formatted",
            "comments",
            "attachments",
        )


class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = (
            "id",
            "hashtag",
            "occurences",
        )


class EventAttachmentSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = EventAttachment
        fields = (
            "id",
            "image_url",
        )

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

class EventSerializer(serializers.ModelSerializer):
    attachments = EventAttachmentSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "date",
            "location",
            "organizer",
            "registered_users",
            "created_at",
            "attachments",
        ]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

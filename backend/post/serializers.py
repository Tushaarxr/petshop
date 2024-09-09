from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Post, PostAttachment, Comment, Trend, Event,EventAttachment,Bookmark


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
#     is_bookmarked = serializers.SerializerMethodField()
#     bookmarks_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Post
#         fields = (
#             'id', 
#             'title', 
#             'description', 
#             'contact_information', 
#             'price', 
#             'category', 
#             'breed', 
#             'color', 
#             'age', 
#             'vaccinated', 
#             'gender', 
#             'weight', 
#             'microchipped', 
#             'trained', 
#             'health_certificate', 
#             'body', 
#             'likes_count', 
#             'comments_count', 
#             'is_bookmarked',  # New field
#             'bookmarks_count',  # New field
#             'created_by', 
#             'created_at_formatted', 
#             'attachments'
#         )

#     def get_is_bookmarked(self, obj):
#         request = self.context.get('request')
#         if request and request.user.is_authenticated:
#             user = request.user
#             return Bookmark.objects.filter(post=obj, user=user).exists()
#         return False

#     def get_bookmarks_count(self, obj):
#         return obj.bookmarks.count()

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    attachments = PostAttachmentSerializer(read_only=True, many=True)
    is_bookmarked = serializers.SerializerMethodField()
    bookmarks_count = serializers.SerializerMethodField()

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
            'is_bookmarked',  # New field
            'bookmarks_count',  # New field
            'created_by', 
            'created_at_formatted', 
            'attachments'
        )

    def get_is_bookmarked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            return Bookmark.objects.filter(post=obj, user=user).exists()
        return False

    def get_bookmarks_count(self, obj):
        return obj.bookmarks.count()

    def update(self, instance, validated_data):
        # Update post fields
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.contact_information = validated_data.get('contact_information', instance.contact_information)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.color = validated_data.get('color', instance.color)
        instance.age = validated_data.get('age', instance.age)
        instance.vaccinated = validated_data.get('vaccinated', instance.vaccinated)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.microchipped = validated_data.get('microchipped', instance.microchipped)
        instance.trained = validated_data.get('trained', instance.trained)
        instance.health_certificate = validated_data.get('health_certificate', instance.health_certificate)
        instance.body = validated_data.get('body', instance.body)

        # Save the updated instance
        instance.save()
        return instance


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
            'attachments',
            'comments'  # Add the 'comments' field here
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



from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from account.models import User, FriendshipRequest
from account.serializers import UserSerializer
from notification.utils import create_notification
from .forms import PostForm, AttachmentForm, EventForm,EventAttachmentForm
from .models import Post, Like, Comment, Trend, Event,Bookmark
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer, TrendSerializer, EventSerializer


@api_view(['GET'])
def post_list(request):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    posts = Post.objects.filter(created_by_id__in=list(user_ids))

    trend = request.GET.get('trend', '')

    if trend:
        posts = posts.filter(body__icontains='#' + trend).filter(is_private=False)

    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def post_detail(request, pk):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    # Remove the is_private condition from the filter
    post = Post.objects.filter(created_by_id__in=list(user_ids)).get(pk=pk)

    return JsonResponse({
        'post': PostDetailSerializer(post).data
    })


@api_view(['GET'])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by_id=id)

    if not request.user in user.friends.all():
        posts = posts.filter(is_private=False)

    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)

    can_send_friendship_request = True

    if request.user in user.friends.all():
        can_send_friendship_request = False

    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)

    if check1 or check2:
        can_send_friendship_request = False

    return JsonResponse({
        'posts': posts_serializer.data,
        'user': user_serializer.data,
        'can_send_friendship_request': can_send_friendship_request
    }, safe=False)


@api_view(['POST'])
def post_create(request):
    form = PostForm(request.POST)
    attachment = None
    attachment_form = AttachmentForm(request.POST, request.FILES)

    if attachment_form.is_valid():
        attachment = attachment_form.save(commit=False)
        attachment.created_by = request.user
        attachment.save()

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        if attachment:
            post.attachments.add(attachment)

        user = request.user
        user.posts_count = user.posts_count + 1
        user.save()

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add something here later!...'})


@api_view(['POST'])
def post_like(request, pk):
    post = Post.objects.get(pk=pk)

    if not post.likes.filter(created_by=request.user):
        like = Like.objects.create(created_by=request.user)

        post = Post.objects.get(pk=pk)
        post.likes_count = post.likes_count + 1
        post.likes.add(like)
        post.save()

        notification = create_notification(request, 'post_like', post_id=post.id)

        return JsonResponse({'message': 'like created'})
    else:
        return JsonResponse({'message': 'post already liked'})


@api_view(['POST'])
def post_create_comment(request, pk):
    comment = Comment.objects.create(body=request.data.get('body'), created_by=request.user)

    post = Post.objects.get(pk=pk)
    post.comments.add(comment)
    post.comments_count = post.comments_count + 1
    post.save()

    notification = create_notification(request, 'post_comment', post_id=post.id)

    serializer = CommentSerializer(comment)

    return JsonResponse(serializer.data, safe=False)


@api_view(['DELETE'])
def post_delete(request, pk):
    post = Post.objects.filter(created_by=request.user).get(pk=pk)
    post.delete()

    return JsonResponse({'message': 'post deleted'})


@api_view(['POST'])
def post_report(request, pk):
    post = Post.objects.get(pk=pk)
    post.reported_by_users.add(request.user)
    post.save()

    return JsonResponse({'message': 'post reported'})


@api_view(['GET'])
def get_trends(request):
    serializer = TrendSerializer(Trend.objects.all(), many=True)

    return JsonResponse(serializer.data, safe=False)




@api_view(['GET', 'POST'])
def event_list_create(request):
    if request.method == 'GET':
        events = Event.objects.all().order_by('-date')
        serializer = EventSerializer(events, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == 'POST':
        form = EventForm(request.POST)
        attachment_form = EventAttachmentForm(request.POST, request.FILES)

        if attachment_form.is_valid():
            attachment = attachment_form.save(commit=False)
            attachment.created_by = request.user
            attachment.save()
        else:
            attachment = None

        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user      
            event.save()

            if attachment:
                event.attachments.add(attachment)

            serializer = EventSerializer(event)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def event_register(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.user not in event.registered_users.all():
        event.registered_users.add(request.user)
        event.save()
        return JsonResponse({'status': 'registered'}, status=status.HTTP_200_OK)
    return JsonResponse({'status': 'already registered'}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
def bookmark_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if user.is_authenticated:
        bookmark, created = Bookmark.objects.get_or_create(post=post, user=user)
        if created:
            return Response({'message': 'Post bookmarked'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Post already bookmarked'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def bookmarked_posts(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    posts = [bookmark.post for bookmark in bookmarks]
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['PUT'])
def post_edit(request, pk):
    print(f"Request user: {request.user}")
    try:
        post = Post.objects.get(pk=pk)
        if post.created_by != request.user:
            return Response({'error': 'Not authorized to edit this post'}, status=status.HTTP_403_FORBIDDEN)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    form = PostForm(request.data, instance=post)
    attachment_form = AttachmentForm(request.data, request.FILES)

    if attachment_form.is_valid():
        attachment = attachment_form.save(commit=False)
        attachment.created_by = request.user
        attachment.save()
        post.attachments.add(attachment)

    if form.is_valid():
        post = form.save(commit=False)
        post.save()

        serializer = PostSerializer(post)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

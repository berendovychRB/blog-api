from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from posts.models import Post
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from accounts.api.serializers import UserDetailSerializer


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            # 'slug',
            'content',
            'image',
            'publish',
        ]


post_detail_url = HyperlinkedIdentityField(view_name='detail-api', lookup_field='slug')
post_delete_url = HyperlinkedIdentityField(view_name='delete-api', lookup_field='slug')


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    delete_url = post_delete_url
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'slug',
            'user',
            'content',
            'markdown',
            'image',
            'created_at',
            'comments',
            'delete_url'
        ]

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_post(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_markdown(self, obj):
        return obj.get_markdown()


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    delete_url = post_delete_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            # 'slug',
            'user',
            'content',
            'delete_url'
        ]


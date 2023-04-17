import sys
import os

sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoOrm.settings")
import django

django.setup()
from django.db.models import Q, Max, Min
from djangoOrm.insta2.models import (
    User,
    Post,
    File,
)
from dotmap import DotMap  # pip install dotmap


class ModelManager:
    pass


class Model:

    def getUsers(self, user):
        return User.objects.filter(id=user.id).values()

    def saveUser(self, user):
        userSet = User()
        userSet.id = user.id
        userSet.id_num = user.idNum
        userSet.state = user.state
        userSet.name = user.name
        userSet.biography = user.biography
        userSet.followers = user.followers
        userSet.following = user.following
        userSet.profile_url = user.profileUrl
        userSet.post_cnt = user.postsCnt
        userSet.post_cnt_str = user.postsCntStr
        userSet.save()

    def savePosts(self, posts):
        value = []
        for post in posts:
            value.append(
                Post(user_id=post.userId, id=post.postId, orders=post.orders))
        Post.objects.bulk_create(value)

    def getPosts(self, userId):
        # Post.objects.filter(tag_seq=self.tag_seq).values()
        return Post.objects.filter(user_id=userId,
                                   state=0).order_by('orders').values()

    def savePost(self, post):
        postSet = Post.objects.get(seq=post.seq)
        postSet.state = 200
        postSet.id_num = post.idNum
        postSet.uploaded = post.uploaded
        postSet.content = post.content
        postSet.file_cnt = post.fileCnt
        postSet.save()

    def saveFiles(self, files):
        value = []
        for file in files:
            value.append(
                File(
                    is_video        = 0 if file.video == '' else 1,
                    img_url         = file.image,
                    img_fullfname   = file.img_fullfname,
                    img_key         = file.img_key,
                    video_url       = file.video,
                    video_fullfname = file.video_fullfname if file.video_fullfname else '',
                    video_key       = file.video_key if file.video_key else '',
                    post_orders     = file.post_orders,
                    orders          = file.orders,
                    cdn             = file.cdn,
                    uploaded        = file.uploaded,
                    user_id         = file.userId,
                    post_id         = file.postId,
                ))
        File.objects.bulk_create(value)

    #이미지 여러개씩
    def saveFilesImgState(self, files):
        for file in files:
            fileSet = File.objects.get(seq=file.seq)
            fileSet.img_state = file.img_state
            fileSet.save()

    #동영상은 1개씩
    def saveFileVideoState(self, file):
        fileSet = File.objects.get(seq=file.seq)
        fileSet.video_state = file.video_state
        fileSet.save()

    # def savePostAndFiles(self, post, files):
    #     self.saveFiles(files)
    #     self.savePost(post)

    def getFiles(self, user):
        '''
        files = File.objects.filter(user_id=user.id,
                                    img_state=0).order_by('uploaded').values()
        '''
        files = File.objects.filter(
            user_id=user.id).filter(Q(img_state=0) | Q(
                video_state=0)).order_by('uploaded').values()
        files = [DotMap(file) for file in files]
        return [
            file for file in files if file.img_url and len(file.img_url) > 200
        ]

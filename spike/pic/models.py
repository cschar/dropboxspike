from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Scene(models.Model):
    # file will be uploaded to MEDIA_ROOT/pic_uploads
    pic = models.ImageField(upload_to ='pic_uploads/',
                            default = 'pic_uploads/None/no-img.jpg')

class Submission(models.Model):

    gif = models.ImageField(upload_to='submission_uploads/gifs/')
    scene = models.ForeignKey(Scene, null=True)
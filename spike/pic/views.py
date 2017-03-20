from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_http_methods

from pic.models import Scene, Submission


def index(request):
    return render(request, 'pic/index.html',
                  {'all_pics': Scene.objects.all(),
                   'all_subs': Submission.objects.all()})


class ImageUploadForm(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class GifUploadForm(forms.Form):
    gifs = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

@require_http_methods(["POST"])
def upload_pic(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        for file in form.files.getlist('images'):
            m = Scene.objects.create()
            m.pic = file
            m.save()
        return redirect(reverse('index'))

@require_http_methods(["POST"])
def upload_gif(request):
    form = GifUploadForm(request.POST, request.FILES)
    # if form.is_valid():  # form isnt valid?
    for file in form.files.getlist('gifs'):
        m = Submission.objects.create()
        m.scene = Scene.objects.first()
        m.gif = file
        m.save()
    return redirect(reverse('index'))


def scene_list(request):
    scenes = []
    for p in Scene.objects.all():
        scenes.append([{'id': p.id,
                        'url': 'https://localhost:8000/media/' + p.pic.url}])
    return JsonResponse({'scenes': scenes})


def submission_list(request, scene_id):
    submissions = []
    for s in Submission.objects.filter(scene=scene_id):
        submissions.append([{'id': s.id,
                             'gif_url': 'https://localhost:8000/media/' + s.gif.url}])
    return JsonResponse({'submissions': submissions})
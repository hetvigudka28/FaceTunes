from django.shortcuts import render, redirect
from webapp import EmotionDetection
from django.core.paginator import Paginator
from . models import Song, Image
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
import urllib.request
# Create your views here.

def image_upload(request):
    context = dict()
    if request.method == 'POST':
        username = "akhil"
        image_path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
        image = NamedTemporaryFile()
        # image.write(urllib.request.urlopen(path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'  # store image in jpeg format
        image.name = name
        if image is not None:
            obj = Image.objects.create(username=username, image=image)  # create a object of Image type defined in your model
            obj.save()
            context["path"] = obj.image.url  #url to image stored in my server/local device
            context["username"] = obj.username
        else :
            return redirect('/')
        # return redirect('any_url')
    return render(request, 'pictures.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.




def main(request):
    mood = EmotionDetection.func();
    return render(request, 'main.html', {"mood": mood})

def index(request):
    moods = EmotionDetection.func()
    q1 = Song.objects.filter(mood = moods)
    print(q1)
    paginator= Paginator(Song.objects.filter(mood = moods),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # data = Song.objects.filter(mood=mood)
    print(type(moods))
    context={"page_obj":page_obj, "moods":moods}
    return render(request,"index.html",context)

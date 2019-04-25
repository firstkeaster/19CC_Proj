from django.shortcuts import render
from .models import IMG
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img = request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'img_tem/uploadimg.html')

@csrf_exempt
def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    for img in imgs:
        print(img.img.url)
    return render(request, 'img_tem/showimg.html', content)

# Create your views here.

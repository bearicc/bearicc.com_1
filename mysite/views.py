from ipware.ip import get_real_ip
from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import visitor_tracking
from django.http import HttpResponse
from django.template import RequestContext
from .forms import UploadFileForm
from django.conf import settings
import os


def home(request):
    visitor_recent = "Not avaliable"
    # ip = get_real_ip(request)
    # if ip is not None:
    #     visitor = visitor_tracking.objects.filter(ip=ip)
    #     if not visitor:
    #         visitor = visitor_tracking.objects.create(ip=ip, recent=timezone.now())
    #         visitor_recent = visitor.recent
    #         visitor.save()
    #     else:
    #         visitor_recent = visitor[0].recent
    #         visitor[0].update()
    #
    return render(request, 'index.html',
                  {'visitor_total': visitor_tracking.objects.count(),
                   'visitor_recent': visitor_recent})


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def resume(request):
    return render(request, 'resume.html')


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            if (title == ""):
                title = request.FILES['file'].name
            handle_uploaded_file(title, request.FILES['file'])
            return HttpResponse("<h1>File :"+title+" uploaded!</h1>")
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form}, context_instance=RequestContext(request))


def handle_uploaded_file(title, f):
    with open(os.path.join(settings.BASE_DIR, "staticfiles/upload/")+title, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def test(request):
    return render(request, 'test.html')

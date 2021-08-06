from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, DeleteView, UpdateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from .models import Album, Photo

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

@login_required
def GalleryView(request):
    album = request.GET.get('album')

    if album == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(album__name=album)

    albums = Album.objects.all()
    context = {'albums':albums, 'photos':photos}
    return render(request, 'gallery.html', context)

class PhotoView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photo.html'

@login_required
def AddPhotoView(request):
    albums = Album.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['album'] != 'none':
            album = Album.objects.get(id=data['album'])
        elif data['album_new'] != '':
            album, created = Album.objects.get_or_create(name=data['album_new'])
        else:
            album = None

        photo = Photo.objects.create(
            album=album,
            description=data['description'],
            image=image)

        return redirect('gallery')


    context = {'albums': albums}
    return render(request, 'add_photo.html', context)

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'delete_photo.html'
    success_url = reverse_lazy('gallery')

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['album']
    template_name = 'update_photo.html'
    success_url = reverse_lazy('gallery')

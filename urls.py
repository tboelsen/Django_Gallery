from django.urls import path

from .views import HomePageView, GalleryView, PhotoView, AddPhotoView, PhotoDeleteView, PhotoUpdateView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('gallery/', GalleryView, name='gallery'),
    path('photo/<uuid:pk>', PhotoView.as_view(), name='photo'),
    path('add_photo', AddPhotoView, name='add_photo'),
    path('photo/<uuid:pk>/delete/', PhotoDeleteView.as_view(), name='delete_photo'),
    path('photo/<uuid:pk>/update/', PhotoUpdateView.as_view(), name='update_photo'),
]

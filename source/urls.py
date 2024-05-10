from django.urls import path
from .views import index, upload_image, delete_message, admin_page, edit_message
urlpatterns = [
    path('', index, name="main"),
    path('request/id/upload/', upload_image, name="new"),
    path('request/id/admin/', admin_page, name='admin'),
    path('post/<int:pk>/edit/', edit_message,  name='update'),
    path('post/<int:pk>/delete/', delete_message, name='delete')
]
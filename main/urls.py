from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('blog/post/<int:post_id>/', views.post, name="post"),
    path('contact/', views.contact, name="contact"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
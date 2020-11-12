from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('blog/post/<int:post_id>/', views.post, name="post"),
    path('contact/', views.contact, name="contact"),
]
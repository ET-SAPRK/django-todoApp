# todo-drf/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('account/', include('account.urls')),
    path('login/', views.LoginView.as_view()),
    path('', TemplateView.as_view(template_name='index.html')),
 ]

# from django.contrib import admin
# from django.urls import path

# from account import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('login/', views.LoginView.as_view()),
# ]
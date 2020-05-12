from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rate.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('login/', LoginView.as_view(template_name= '/'), name='user_login'),
    path('logout/', LogoutView.as_view(template_name='/'), name="user_logout"),
]
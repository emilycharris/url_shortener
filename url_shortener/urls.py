"""url_shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView

from short_url_app.views import IndexView, CreateUserView, ProfileView, CreateBookmarkView, EditView, RemoveView, DisplayRedirectView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^login/$', LoginView.as_view(), name='login_view'),
    url(r'^create_user/$', CreateUserView.as_view(), name='create_user_view'),
    url(r'^accounts/profile/$', login_required(ProfileView.as_view()), name='profile_view'),
    url(r'^logout/$', LogoutView.as_view(), name='logout_view'),
    url(r'^create_bookmark/$', login_required(CreateBookmarkView.as_view()), name='create_bookmark_view'),
    url(r'^update/(?P<pk>\d+)/$', login_required(EditView.as_view()), name='update_view'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(RemoveView.as_view()), name='delete_view'),
    url(r'^(?P<hashid>\w+)/$', DisplayRedirectView.as_view(), name="redirect_view")
]

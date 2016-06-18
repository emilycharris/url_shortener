from hashids import Hashids
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, TemplateView, ListView, FormView

from short_url_app.models import Click, Bookmark


class IndexView(TemplateView):
    template_name = "index.html"

class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/login"

#@login_required
class CreateBookmarkView(CreateView):
    template_name = 'create_bookmark.html'
    model = Bookmark
    fields = ['url', "description"]
    success_url = "/accounts/profile"

    def form_valid(self, form):
        bookmark = form.save(commit=False)
        bookmark.user = self.request.user
        hashid = Hashids()
        bookmark.hashid = hashid.encode(id(bookmark.url))
        return super(CreateBookmarkView, self).form_valid(form)


class ProfileView(ListView):
    template_name = "profile.html"
    model = Bookmark





class EditView(FormView):
    template_name = "edit.html"

class UrlList(ListView):
    model = Click



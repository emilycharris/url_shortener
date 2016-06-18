from django.utils.decorators import method_decorator
from hashids import Hashids
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, TemplateView, ListView, RedirectView
from django.views.generic.edit import UpdateView, DeleteView

from short_url_app.models import Click, Bookmark



class IndexView(TemplateView):
    template_name = "index.html"

class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/login"

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

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)


class EditView(UpdateView):
    model = Bookmark
    fields = ['url', "description"]
    success_url = "/accounts/profile"

class RemoveView(DeleteView):
    model = Bookmark
    success_url = '/accounts/profile'


class DisplayRedirectView(RedirectView):

    def get(self, request, *args, **kwargs):
        hashid = self.kwargs.get('hashid', None)
        link = Bookmark.objects.get(hashid=hashid)
        self.url = link.url
        link.click_count += 1
        link.save()
        return super(DisplayRedirectView, self).get(request, args, **kwargs)







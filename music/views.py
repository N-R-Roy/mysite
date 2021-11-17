
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.views.generic import View

from .models import Album, Song, Test

from .forms import UserForm, TestForm, LoginForm

from django.contrib.auth.models import User

import math


class IndexView(ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailsView(DetailView):
    template_name = 'music/detail.html'
    model = Album


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class SongCreate(CreateView):
    model = Song
    fields = ['album', 'file_type', 'song_title']


class SongList(ListView):
    template_name = 'music/SongList.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return Song.objects.all()


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # make hash password then set
            user.set_password(password)

            user.save()

            # return user object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


class TestFormView(View):

    form_class = TestForm
    template_name = 'music/test_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            user.name = name
            user.password = password

            user.save()

            obj = Test.objects.get(name=name, password=password)

            if obj is not None:
                return redirect('music:index')

        return render(request, self.template_name, {'form': form})


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'music/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # make hash password then set
            user.set_password(password)

            user.save()

            # return user object if credentials are correct
            user = authenticate(username=username, password=password)

            # user = User.objects.get(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


# This view function use for read file from database and
# Then process this file data and then show output in showdata.html page
def Test_File(request):
    if request.method == "GET":
        record = Album.objects.get(id=14)

        ul_file = record.album_logo

        # data = file.read()  # This is read binary format

        file = ul_file.open(mode='r')

        file_data = ''
        for line in file:
            # line = line + '  HHH  '
            file_data = file_data + line

        # str = '*******This is read from TestEmp.txt file *******<br>'
        #
        # file_data = str + file_data

        # record.delete() # This is use for delete record

        word_list = file_data.split()

        return render(request, 'music/showdata.html', {'word_list': word_list})


class Login(View):
    template_name = 'music/lgin.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        # return user object if credentials are correct
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('music:index')
        else:
            return render(request, 'music/lgin.html', {'rdata': 'Please enter valid username or password'})


def f(v):
    num = pow(5, v)
    result = math.sqrt(num)
    result = "%.2f" % result
    return result


def lgin(request):
    data = f(7)
    return render(request, 'music/lgin.html', {"data": data})


def check_user(request):
    # if request == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    # return user object if credentials are correct
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('music:index')
    else:
        return render(request, 'music/lgin.html', {'rdata': 'Please enter valid username or password'})


def LogOut(request):
    if request == 'GET':
        logout(request)
        return redirect('music:login')

















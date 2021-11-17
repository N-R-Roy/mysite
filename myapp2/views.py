
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import RenewBookForm

from .models import UserInfo


class MyView(generic.View):
    template_name = 'myapp2/myview.html'

    def get(self, request):
        return render(request, self.template_name, {'text': "Hello World!"})


class MyView2(generic.TemplateView):
    template_name = "myapp2/myview2.html"


def index(request):
    return render(request, 'myapp2/index.html')


def display(request, user_address):

    users = list(UserInfo.objects.filter(address=user_address))

    context = {
        'users': users,
    }

    return render(request, 'myapp2/display.html', context)


def show(request):
    return render(request, 'myapp2/show.html')


def result(request):
    if request.method == 'POST':
        num1 = int(request.POST['txt_num1'])
        num2 = int(request.POST['txt_num2'])

        sum = num1 + num2

        return render(request, 'myapp2/result.html', {'sum': sum})


def add_user(request):
    return render(request, 'myapp2/add_user.html')


def add_user_info(request):
    if request.method == 'POST':
        uname = request.POST['user_name']
        uaddress = request.POST['user_address']
        uhobby = request.POST['user_hobby']

        user_entry = UserInfo(name=uname, address=uaddress, hobby=uhobby)
        user_entry.save()

        return HttpResponseRedirect(reverse('myapp2:add_user'))


def ajax_page(request):
    return render(request, 'myapp2/ajax_page.html')


def ajax_sum(request):

    if request.method == 'POST':

        num1 = request.POST['nmb1']
        num2 = request.POST['nmb2']

        sm = num1 + num2

        return HttpResponse(sm)


class TestForm(generic.View):
    form_class = RenewBookForm
    template_name = 'myapp2/test_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})









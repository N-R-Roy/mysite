
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import EmpInfo


# This is for index page
def index(request):

    return render(request, 'myapp/index.html')


# This is for display page
def display(request):
    return render(request, 'myapp/display.html')


# This is for show page
def show(request, num):
    name = 'N.R.Roy' + ' ' + str(num)
    context = {'name': name}
    return render(request, 'myapp/show.html', context)


# This is for printt page
def printt(request, num1, num2):
    name = num1 + num2
    context = {
        'num1': num1,
        'num2': num2,
        'name': name,
    }
    return render(request, 'myapp/printt.html', context)


# This is for flower page
def flower(request):
    return render(request, 'myapp/flower.html')


# This view function take data from bird and show this to the flower page
def tname(request):
    text = str(request.POST['txt'])

    from nltk import word_tokenize

    token = word_tokenize(text)

    context = {'token': token}

    return render(request, 'myapp/flower.html', context)


# This is for fruit page
def fruit(request):
    return render(request, 'myapp/fruit.html')


# This is for animal page
def animal(request):
    emp_list = EmpInfo.objects.all()  # Query data from database
    context = {'emp_list': emp_list}
    return render(request, 'myapp/animal.html', context)


# This is for fish page
def fish(request):
    return render(request, 'myapp/fish.html')


# This is for bird page
def bird(request):
    if request.method == 'GET':
        return render(request, 'myapp/bird.html')


# This is for tree page
def tree(request):
    txt = show_tree()
    context = {
        'text': txt,
    }
    return render(request, 'myapp/Tree.html', context)


# This is user define function
def show_tree():
    return 'This is show tree'


def add(request):
    if request.method == 'POST':
        nm1 = int(request.POST['num1'])
        nm2 = int(request.POST['num2'])

        rslt = nm1 + nm2

        return render(request, 'myapp/result.html', {'result': rslt})


def empinfo(request):
    if request.method == 'GET':
        emp_list = EmpInfo.objects.all()
        context = {
            'emp_list': emp_list
        }
        return render(request, 'myapp/EmpInfo.html', context)


# This function show insert page
def insert(request):
    return render(request, 'myapp/insert.html')


class CountryView(generic.TemplateView):
    template_name = 'myapp/country.html'


# This function take data from insert page and then insert into database
def insert_data(request):

    if request.method == 'POST':
        emp_name = request.POST['txtname']
        emp_address = request.POST['txtaddress']
        emp_dept = request.POST['txtdept']

        emp = EmpInfo(name=emp_name, address=emp_address, dept=emp_dept)
        emp.save()

        return render(request, 'myapp/insert.html')


# This function show search page
def search(request):
    return render(request, 'myapp/search.html')


def search_data(request):
    if request.method == 'POST':
        sname = request.POST['srchname']

        emp = EmpInfo.objects.get(name=sname)

        context = {'emp': emp}

        return render(request, 'myapp/search.html', context)


# This function show search page
def update(request):
    return render(request, 'myapp/update.html')


def update_data(request):
    if request.method == 'POST':
        uname = request.POST['upname']
        uaddress = request.POST['upaddress']

        emp = EmpInfo.objects.get(name=uname)

        emp.address = uaddress

        emp.save()

        return render(request, 'myapp/update.html')


# This function show delete page
def delete(request):
    return render(request, 'myapp/delete.html')


def delete_data(request):
    if request.method == 'POST':
        del_name = request.POST['dname']

        emp = EmpInfo.objects.get(name=del_name)
        emp.delete()

        return render(request, 'myapp/delete.html')
































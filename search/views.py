from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic

from .models import Class
from login.models import Student, Advisor
from .forms import ClassForm, ClassInfoForm

import requests

URL_BASE = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearchOptions?institution=UVA01&term=1232'

def search_view(request):
    advisorCheck = False
    advisors=Advisor.objects.all()
    for each in advisors:
        if request.user.email == each.email:
            advisorCheck = True

    r = requests.get(URL_BASE)
    # pass in department names and ids before loading search page
    context = {
         'depts': [ {'subject': s['subject'], 'descr': s['descr']} for s in r.json()['subjects']],
         'advisorCheck' : advisorCheck
    }
    return render(request, 'search.html', context)

# ideally use AJAX.
def search_class_view(request):
    advisorCheck = False
    advisors=Advisor.objects.all()
    for each in advisors:
        if request.user.email == each.email:
            advisorCheck = True

    url = URL_BASE
    r = requests.get(url)
    # pass in department names and ids before loading search page
    search=True
    context = {
        'depts': [ {'subject': s['subject'], 'descr': s['descr']} for s in r.json()['subjects']],
        'advisorCheck' : advisorCheck,
        'search' : search,
    }
    url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&page=1'
    if request.method == 'POST':
        form = ClassForm(request.POST)
        data = form.data
        # url += "&term=" + data['semester']
        if data['subject']:
            url += "&subject=" + data['subject']
        if data['descr']:
            url += "&keyword=" + data['descr']
        if data['catalog_nbr']:
            url += "&catalog_nbr=" + data['catalog_nbr']

        r = requests.get(url)
        classes=r.json()
        usr = Student.objects.get(email=request.user.email)
        cartClasses = usr.cart.classes.all()
        for each in classes:
            if cartClasses:
                for every in cartClasses:
                    if  every.crse_id == int(each['crse_id']) and every.class_section ==  int(each['class_section']):
                        each['cart']=True
                        break
                    else:
                        each['cart']=False
            else:
                each['cart']=False
        context['classes'] = classes
        return render(request, 'search.html', context)

def search_add_view(request):
    advisorCheck = False
    advisors=Advisor.objects.all()
    for each in advisors:
        if request.user.email == each.email:
            advisorCheck = True

    url = URL_BASE
    r = requests.get(url)
    # pass in department names and ids before loading search page
    context = {
        'depts': [ {'subject': s['subject'], 'descr': s['descr']} for s in r.json()['subjects']],
        'advisorCheck' : advisorCheck
    }
    if request.method == 'POST':
        form = ClassInfoForm(request.POST)
        data = form.data
        try:
            cls = Class.objects.get(crse_id = data['crse_id'], class_section = data['class_section'])
        except:
            cls = Class.objects.create(subject = data['subject'],
                catalog_nbr = data['catalog_nbr'],
                descr = data['descr'],
                crse_id = data['crse_id'],
                class_section = data['class_section'],
                days = data['days'], 
                start_time = data['start_time'], 
                end_time = data['end_time']) 
        student = Student.objects.get(username=request.user.username)
        student.cart.classes.add(cls)             
        return render(request, 'search.html', context)
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
import json

from search.models import Class
from schtools.models import Cart, Schedule
from login.models import Student, Advisor
import requests
from .helper import format_cart, format_schedules, get_times, no_conflict, zip_times
from .forms import ScheduleForm
from django.contrib import messages

def tools_view(request):
    advisorCheck = False
    advisors=Advisor.objects.all()
    for each in advisors:
        if request.user.email == each.email:
            usr = Advisor.objects.get(email=request.user.email)
            advisorCheck = True
    if advisorCheck:
        schedAdvisor = usr.schedules.all()
        allClasses= dict()
        for each in schedAdvisor:
            classes = each.classes.all()
            allClasses[each]=classes
        context = {
            'advisorCheck' : advisorCheck,
            'schedAdvisor' : schedAdvisor,
            'allClasses' : allClasses
        }
        return render(request, 'sched_tools.html', context)
    usr = Student.objects.get(username=request.user.username)
    cart = usr.cart
    schedules = usr.schedules
    sched_select=False
    request.session['sch_name'] = ''
    for each in schedules.all():
        if each.name == request.session['sch_name']:
            sched_select=True
    advisor = usr.advisor_set.all().first() 
    context = {
        'user_cart' : format_cart(cart.classes.all()),
        'schedules' : format_schedules(schedules.all(), advisor),
        'sched_select' : sched_select
    }
    return render(request, 'sched_tools.html', context)

def delete_cart_view(request, id):
    usr = Student.objects.get(username=request.user.username)
    cls = Class.objects.get(id=id)
   
    usr.cart.classes.remove(cls)
    cart = usr.cart
    schedules = usr.schedules
    sched_select=False
    for each in schedules.all():
        if each.name == request.session['sch_name']:
            sched_select=True
    advisor = usr.advisor_set.all().first() 
    context = {
        'user_cart' : format_cart(cart.classes.all()),
        'schedules' : format_schedules(schedules.all(), advisor),
        'sched_select' : sched_select
    }
    return render(request, 'sched_tools.html', context)

def create_schedule_view(request):
    usr = Student.objects.get(username=request.user.username)
    cart = usr.cart
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        name = form.data['name']
        try:
            _ =  usr.schedules.get(name=name)
        except:
            sch = Schedule.objects.create(name=name, studentFirstName=usr.firstname, studentLastName=usr.lastname)
            usr.schedules.add(sch)
    schedules = usr.schedules
    sched_select=False
    for each in schedules.all():
        if each.name == request.session['sch_name']:
            sched_select=True
    advisor = usr.advisor_set.all().first() 
    context = {
        'user_cart' : format_cart(cart.classes.all()),
        'schedules' : format_schedules(schedules.all(), advisor),
        'sched_select' : sched_select
    }
    return render(request, 'sched_tools.html', context)

def select_view(request):
    usr = Student.objects.get(username=request.user.username)
    cart = usr.cart
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        sch_name = form.data['schedule']
        sch =  usr.schedules.get(name=sch_name)
        request.session['sch_name'] = sch.name
        request.session['classes'] = format_cart(sch.classes.all())
    schedules = usr.schedules
    sched_select=False
    for each in schedules.all():
        if each.name == request.session['sch_name']:
            sched_select=True
    advisor = usr.advisor_set.all().first() 
    context = {
        'user_cart' : format_cart(cart.classes.all()),
        'schedules' : format_schedules(schedules.all(), advisor),
        'sched_select' : sched_select
    }
    return render(request, 'sched_tools.html', context)

def remove_class_view(request, id):
    sch_name = request.session.get('sch_name') 
    usr = Student.objects.get(username=request.user.username)
    schedule = usr.schedules.get(name=sch_name)
    cls = Class.objects.get(id=id)
    schedule.classes.remove(cls)
    cart = usr.cart
    schedules = usr.schedules
    sched_select=False
    for each in schedules.all():
        if each.name == request.session['sch_name']:
            sched_select=True
    advisor = usr.advisor_set.all().first() 
    request.session['classes'] = format_cart(schedule.classes.all())
    context = {
        'user_cart' : format_cart(cart.classes.all()),
        'schedules' : format_schedules(schedules.all(), advisor),
        'sched_select' : sched_select
    }
    return render(request, 'sched_tools.html', context)

def add_class_view(request):
        usr = Student.objects.get(username=request.user.username)
        schedules = usr.schedules
        sched_select=False
        for each in schedules.all():
            if each.name == request.session['sch_name']:
                sched_select=True
        advisor = usr.advisor_set.all().first() 
        cart = usr.cart
        context = {
            'user_cart' : format_cart(cart.classes.all()),
            'schedules' : format_schedules(schedules.all(), advisor),
            'sched_select' : sched_select
        }
        sch_name = request.session.get('sch_name') 
        if sch_name is None:
            messages.info(request, 'Select a schedule!')
        else:
            schedule = usr.schedules.get(name=sch_name)
            if request.method == 'POST':
                form = ScheduleForm(request.POST)
                sch_times = get_times(schedule.classes.all())
                classes = cart.classes.all()
                add_flag = True
                if not classes:
                    messages.info(request, 'Select classes to add to schedule!')
                else:
                    for cls in classes:
                        try:
                            checked = form.data['check' + str(cls.id)]
                            if checked:
                                cls_times = get_times([cls])
                              
                                if no_conflict(cls_times, sch_times):
                                    sch_times = zip_times(sch_times, cls_times)
                                else:
                                    messages.info(request, 'Cannot add classes due to schedule conflict!')
                                    add_flag = False
                                    break
                        except:
                            pass
                    if add_flag:
                        for cls in classes:
                            try:
                                checked = form.data['check' + str(cls.id)]
                                if checked:
                                    schedule.classes.add(cls)
                            except:
                                pass
                        request.session['classes'] = format_cart(schedule.classes.all())
        return render(request, 'sched_tools.html', context)

def toggle_share_schedule_view(request, id):
        usr = Student.objects.get(username=request.user.username)
        cart = usr.cart
        schedules = usr.schedules
        sched_select=False
        for each in schedules.all():
            if each.name == request.session['sch_name']:
                sched_select=True
        advisor = usr.advisor_set.all().first() 
        sch = schedules.get(id=id)
        if advisor.schedules.filter(id=id):
            advisor.schedules.remove(sch)
        else:
            advisor.schedules.add(sch)
        context = {
            'user_cart' : format_cart(cart.classes.all()),
            'schedules' : format_schedules(schedules.all(), advisor),
            'sched_select' : sched_select
        }
        return render(request, 'sched_tools.html', context)

def delete_schedule_view(request, id):
    Schedule.objects.filter(id=id).delete()
    usr = Student.objects.get(username=request.user.username)
    cart = usr.cart
    schedules = usr.schedules
    sched_select=False
    for each in schedules.all():
        if each.name == request.session['sch_name']:
            sched_select=True
    schedule = schedules.all().first()
    if schedules.all().first():
        request.session['sch_name'] = schedule.name
    else:
        request.session['sch_name'] = None
    advisor = usr.advisor_set.all().first() 
    context = {
        'user_cart' : format_cart(cart.classes.all()),
        'schedules' : format_schedules(schedules.all(), advisor),
        'sched_select' : sched_select
    }
    return render(request, 'sched_tools.html', context)

def advisor_approve(request, id):
    usr = Advisor.objects.get(email=request.user.email)
    schedule = Schedule.objects.get(id=id)
    schedule.rejected = False
    schedule.approved = True
    schedule.save()
    usr.schedules.remove(usr.schedules.get(id=id))
    return HttpResponseRedirect(reverse('Tools'))

def advisor_reject(request, id):
    usr = Advisor.objects.get(email=request.user.email)
    schedule = Schedule.objects.get(id=id)
    schedule.rejected = True
    schedule.approved = False
    schedule.save()
    usr.schedules.remove(usr.schedules.get(id=id))
    return HttpResponseRedirect(reverse('Tools'))



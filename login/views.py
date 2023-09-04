from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from login.models import User, Student, Advisor
from schtools.models import Cart
from .forms import profileForm

import requests
# admin accounts are directred to admin page
# advisor and student accounts are directed to seperate pages

def user_redirect(request):
    if request.user.is_authenticated:
        advisorCheck = False
        advisors=Advisor.objects.all()
        for each in advisors:
            if request.user.email == each.email:
                advisorCheck = True
        context = {
            'advisorCheck' : advisorCheck
        }
        if request.user.is_superuser:
            return redirect('/admin')
        
        if advisorCheck:
                    usr = Advisor.objects.get(email=request.user.email)
                    return render(request, 'advisor.html', context)
        try:
                    usr = Student.objects.get(email=request.user.email)
                    return render(request, 'student.html', context)
        except (Student.DoesNotExist):
                    cart = Cart.objects.create()
                    advisor = Advisor.objects.get(username="default")
                    usr = Student.objects.create(
                            email=request.user.email, username=request.user.username, studentID ='', 
                            major='', firstname=request.user.first_name, lastname=request.user.last_name, cart=cart)
                    usr.advisor_set.add(advisor)
                    return render(request, 'student.html', context)
    return render(request, 'home.html')

def profile_view(request):
    all_Students = Student.objects.all()
    student_list = list()
    for each in all_Students:
        if each.username == request.user.username:
            student_list.append(each)
    context = {
        'students' : student_list,
    }
    return render(request, 'profile.html', context)

def profile_edit_view(request):
    all_Students = Student.objects.all()
    student_list = list()
    for each in all_Students:
        if each.username == request.user.username:
            student_list.append(each)
    context = {
        'students' : student_list,
    }
    return render(request, 'edit_profile.html', context)

def submit_edits_view(request):
    all_Students = Student.objects.all()
    for each in all_Students:
        if request.user.username == each.username:
            if request.method == 'POST':
                form = profileForm(request.POST)
                data = form.data
                each.firstname = data['first_name']
                each.lastname = data['last_name']
                each.studentID = data['student_id']
                each.major = data['major']
                each.save()
    return HttpResponseRedirect(reverse('profile'))
       
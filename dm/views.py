from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model


from dm.models import Message

from login.models import User, Advisor, Student


def index(request):
    username= request.user.username
    inbox_list= list()
    inbox_names= list()
    users=list()
    seen=list()

    try:
        usr = Advisor.objects.get(username=username)
        advisorCheck = True
        inbox_list= usr.students.all()
        

    except Advisor.DoesNotExist:
        advisorCheck = False
        usr= Student.objects.get(username=username)
        inbox_list= usr.advisor_set.all()

    for each in inbox_list:
        inbox_names.append(each.username)
        #print(each.username)
    
   

    for each in  get_user_model().objects.all():
        if (each.username in inbox_names):
            users.append(each)

    '''
    for each in users:
        print(each.username)
    

    for each in users:
        the_great_filter = (
            f'chat_{each.id}_{request.user.id}'
        )
        try:
             seen.append((Message.objects.filter(thread_name=the_great_filter).latest("timestamp")).viewed)
             #seen.append(messages[-1].viewed)
        except Message.DoesNotExist: 
            seen.append(True)
            
    

    x=zip(users, seen)

    print("-------")
    for each, see in x:
        print(each.username)
        print(see)
        print("------")

    '''

    context = {'users': users,
        'advisorCheck': advisorCheck,
        'username': username,
    }

    
    return render(request, 'dm-list.html', context)


def chat_page(request, username):
    
    user_object = get_user_model().objects.get(username=username)
    username= request.user.username
    print(username)
    
    inbox_list= list()
    inbox_names= list()
    users=list()
    seen=list()
    messages2=list()
    messages3=list()

    try:
        usr = Advisor.objects.get(username=username)
        advisorCheck = True
        print(usr.username)
        inbox_list= usr.students.all()
        

    except Advisor.DoesNotExist:
        advisorCheck = False
        usr= Student.objects.get(username=username)
        inbox_list= usr.advisor_set.all()
        
       
    for each in inbox_list:
        inbox_names.append(each.username)
    
    #print("new")
    for each in  get_user_model().objects.all():
        if (each.username in inbox_names):
            users.append(each)


    thread_name = (
            f'chat_{request.user.id}_{user_object.id}'
            if int(request.user.id) > int(user_object.id)
            else f'chat_{user_object.id}_{request.user.id}'
        )
    
    messages = Message.objects.filter(thread_name=thread_name).order_by("timestamp")


    '''
    #check for new messages for notifications bar
    for each in users:
        the_great_filter = (
            f'chat_{each.id}_{request.user.id}'
        )
        try:
             if (each.id == user_object.id):
                Message.objects.filter(thread_name=the_great_filter).update(viewed=True)
                 
             seen.append((Message.objects.filter(thread_name=the_great_filter).latest("timestamp")).viewed)
             #seen.append(messages2[-1].viewed)
        except Message.DoesNotExist: 
            seen.append(True)


    x=  zip(users, seen)
    
   

    '''
    


    print("hello")
    print(advisorCheck)
    context = {
        'users': users,
        'user_object': user_object,
        'messages': messages,
        'advisorCheck': advisorCheck,
    }

    return render(request, 'dm-detail.html', context)

'''
def share_schedule(request, username, id):
        
    user_object = get_user_model().objects.get(username=username)
    advusername=username
    username= request.user.username
    inbox_list= list()
    inbox_names= list()
    users=list()
    seen=list()
   

    try:
        usr = Advisor.objects.get(username=username)
        advisorCheck = True
        inbox_list= usr.students.all()

        
    except Advisor.DoesNotExist:
        advisorCheck = False
        usr= Student.objects.get(username=username)
        schedules = usr.schedules
        inbox_list= usr.advisor_set.all()
        advisor= usr.advisor_set.all().get(username=advusername)
        sch = schedules.get(id=id)
        advisor.schedules.add(sch)
        
        
    for each in inbox_list:
        inbox_names.append(each.username)
    
    #print("new")
    for each in  get_user_model().objects.all():
        if (each.username in inbox_names):
            users.append(each)


    thread_name = (
            f'chat_{request.user.id}_{user_object.id}'
            if int(request.user.id) > int(user_object.id)
            else f'chat_{user_object.id}_{request.user.id}'
        )
    
    messages = Message.objects.filter(thread_name=thread_name).order_by("timestamp")
        
    context = {
        'users': users,
        'user_object': user_object,
        'messages': messages,
        'adivosrCheck': advisorCheck,
        'schedules': schedules,
    }

    return render(request, 'dm-detail.html', context)
    

'''




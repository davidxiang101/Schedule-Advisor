from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic

from login.models import Student
from schtools.models import Schedule

def cal_view(request):
        usr = Student.objects.get(username=request.user.username)
        schedules = usr.schedules.all()
        
        context = {
            'schedules' : schedules,
        }
        return render(request, 'calendar.html', context)

def display_view(request, id):
        usr = Student.objects.get(username=request.user.username)
        schedules = usr.schedules.all()

        try:
            sch_item = Schedule.objects.get(id=id)
        except (Schedule.DoesNotExist):
            context = {
            'schedules' : schedules,
            }
            return render(request, 'calendar.html', context)
        
        days_shrt = ['Mo', 'Tu', 'We', 'Th', 'Fr']
        day_dict = {'Mo' : 'Monday', 'Tu' : 'Tuesday', 'We' : 'Wednesday', 'Th' : 'Thursday','Fr' : 'Friday'}
        day_to_num = {'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, 'Friday' : 5}
        scheduled_classes = []
        colors = ['#845EC2', '#0081CF', '#008F7A', '#D65DB1', '#FF6F91', '#FF9671', '#FFC75F']
        color_index = 0
        class_to_color = {}
        events = []
        for course in sch_item.classes.all():
            start_times_raw = course.start_time.split(',')
            end_times_raw = course.end_time.split(',')
            # days grouped by start times
            day_grps = course.days.split(',')
            for i in range(len(start_times_raw)):
                start_time = start_times_raw[i].strip()
                end_time = end_times_raw[i].strip()
                days = day_grps[i].strip()
                if start_time == '' or end_time == '' or days == '':
                    break
                
                # parsing string format
                start_hour = int(start_time[:2])
                start_minute = int(start_time[3:5])
                end_hour = int(end_time[:2])
                end_minute = int(end_time[3:5]) 
                times = []
                for day_ in days_shrt:
                    if day_ in days:
                        title = str(course.subject) + ' ' + str(course.catalog_nbr)
                        if title not in class_to_color:
                            class_to_color[title] = colors[color_index]
                            color_index += 1
                            #if the color index gets out of range restart
                            if (color_index == 7):
                                 color_index == 0
                        day = day_dict[day_]
                        day_num = day_to_num[day]
                        d = '2023-05-0' + str(day_num) + 'T'
                        events.append({'title': str(course.subject) + ' ' + str(course.catalog_nbr),
                                       'start': d + f"{start_hour:02}" + ':' + f"{start_minute:02}" + ':00',
                                       'end': d + f"{end_hour:02}" + ':' + f"{end_minute:02}" + ':00',
                                       'color': class_to_color[title]})
        context= {
             'evs':events,
             'sch_name': sch_item.name,
             'schedules' : schedules,
        }
                
        return render(request, 'calendar.html', context)
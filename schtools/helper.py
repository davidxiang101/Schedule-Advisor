def format_cart(classes_raw):
    formatted_classes = []
    for course in classes_raw:
        times = ''

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
            start_time = start_time[:2] + ":" + start_time[3:5]
            end_time = end_time[:2] + ":" + end_time[3:5] 
            times += days + ' ' + start_time + '-' + end_time + ', '
        times = times[:-2]
        cls = {'times': times, 'subject': course.subject,
                'catalog_nbr': course.catalog_nbr, 'id': course.id}           
        formatted_classes.append(cls)
    return formatted_classes

# return a dictionary keys: days items: list of start and end times
def get_times(classes_raw):
    days = ['Mo', 'Tu', 'We', 'Th', 'Fr', "Sa", 'Su']
    times = {day: {'start' : [], 'end' : []} for day in days}
    for course in classes_raw:
        start_times_raw = course.start_time.split(',')
        end_times_raw = course.end_time.split(',')
        # days grouped by start times
        day_grps = course.days.split(',')
        for i in range(len(start_times_raw)):
            start_time = start_times_raw[i].strip()
            end_time = end_times_raw[i].strip()
            days_ = day_grps[i].strip()
            if start_time == '' or end_time == '' or days_ == '' or days_ =='-':
                break
            
            # parsing string format into integers
            
            start_time = int(start_time[:2]) * 100 + int(start_time[3:5])
            end_time = int(end_time[:2]) * 100 + int(end_time[3:5])

            for day in days:
                if day in days_:
                    times[day]['start'].append(start_time)
                    times[day]['end'].append(end_time)
    return times

# zips to times together
# assumes no conflicts 
def zip_times(times1, times2):
    for day in times1:
        times2[day]['start'] += times1[day]['start']
        times2[day]['end'] += times1[day]['start']
    return times2

# check for no conflict between times
# does not check for internal conflicts!!
def no_conflict(times1, times2):
    for day in times1:
       
        for i in range(len(times1[day]['start'])):
            
            for j in range(len(times2[day]['start'])):
           
                if times2[day]['start'][j] <= times1[day]['start'][i] <= times2[day]['end'][j]:
               
                    return False
                elif times1[day]['start'][i] <= times2[day]['start'][j] <= times1[day]['end'][i]:
                  
                    return False
    return True


def format_schedules(schedules_raw, advisor):
    formatted_schedules = []
    schedules = advisor.schedules.all()
    for sch_ in schedules_raw:
        sch = {'id': sch_.id, 'rejected': sch_.rejected, 'approved': sch_.approved, 'name': sch_.name, 'sent': False,
                'studentFirstName': sch_.studentFirstName, 'studentLastName': sch_.studentLastName}
        if schedules.filter(id=sch_.id):
            sch['sent'] = True           
        formatted_schedules.append(sch)
    return formatted_schedules
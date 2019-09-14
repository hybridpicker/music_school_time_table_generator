from datetime import time, timedelta

class Student():
    def __init__(self, first_name, 
                 last_name, minutes, preferred_day, 
                 from_time, till_time):
        self.first_name = first_name
        self.last_name = last_name
        self.minutes = minutes
        self.preferred_day = preferred_day
        self.from_time = from_time
        self.till_time = till_time
        
    def blocked_min_list(list_obj, day, key):
        string = result[day][key][0]
        hours = string[0:2]
        minutes = string[3:5]
        x = timedelta(hours=int(hours), minutes=int(minutes))
        # add every minute already used in list
        while str(x) not in result[day][key][1]:
            list_obj.append(str(x))
            x += timedelta(minutes = 1)      
        list_obj.sort()
        return list_obj
    
    def blocked_min_list_new_items(list_obj, from_time, till_time):
        string = from_time
        hours = string[0:2]
        minutes = string[3:5]
        x = timedelta(hours=int(hours), minutes=int(minutes))
        # add every minute already used in list
        while str(x) != till_time:
            list_obj.append(str(x))
            x += timedelta(minutes = 1)      
        list_obj.sort()
        return list_obj
    
    def generate_time():
        for day in week_days:
            i = 0
            blocked_min = []
            # Check if dict is not empty
            if bool(result[day]) is True:
                # get latest index out of dict
                i = int(sorted(result[day].keys())[-1])
                for key in result[day]:
                    blocked_min = blocked_min_list(blocked_min, day, key)
            for student in students:
                student_name = student.first_name + " " + student.last_name
                from_time = str(student.from_time)
                till_time = str(student.from_time + student.minutes)
                if from_time in blocked_min or till_time in blocked_min:
                    y = student.from_time
                    while str(y) in blocked_min:
                        y += timedelta(minutes = 1)
                        # Check if Time ist bigger than the current day
                        if y >= timedelta(minutes = 59, hours = 23):
                            print('Not possible: ' + student_name)
                            break
                        
                    student_from_time = y
                    student_till_time = (student.from_time + student.minutes) + (y - student.from_time)
                    student_list = [str(student_from_time), str(student_till_time), student_name]
                    """
                    After saving new block update blocked_min_list
                    """
                    # Check if saved time is already in blocked_min
                    if str(student_from_time) not in blocked_min or str(student_till_time) not in blocked_min:
                        blocked_min = Student.blocked_min_list_new_items(blocked_min, 
                                                                         str(student_from_time), 
                                                                         str(student_till_time))
                    else:
                        pass

                else:
                    """
                    Preferred time is not in blocked min -> Check latest possibility
                    """
                    student_till_time = student.from_time + student.minutes
                    from_time = str(student.from_time)
                    student_list = [str(student.from_time), str(student_till_time), student_name]
                    # Check if saved time is already in blocked_min
                    if str(from_time) not in blocked_min or str(student_till_time) not in blocked_min:
                        blocked_min = Student.blocked_min_list_new_items(blocked_min, 
                                                                         str(from_time), 
                                                                         str(student_till_time))
                result[day][i] = student_list
                i += 1
    
s1 = Student('John', 'Clarke', timedelta(minutes = 25), 0, timedelta(hours = 14, minutes = 0), None)
s2 = Student('Marta', 'Biss', timedelta(minutes = 25), 0, timedelta(hours = 13, minutes = 0), None)
s3 = Student('John', 'Doe', timedelta(minutes = 25), 0, timedelta(hours = 12, minutes = 20), None)
s4 = Student('Luke', 'Ratford', timedelta(minutes = 25), 0, timedelta(hours = 11, minutes = 30), None)
s5 = Student('John', 'Snow', timedelta(minutes = 25), 0, timedelta(hours = 13, minutes = 0), None)
s6 = Student('Mr', 'X', timedelta(minutes = 25), 0, timedelta(hours = 15, minutes = 30), None)
s7 = Student('John', 'Clarke', timedelta(minutes = 25), 0, timedelta(hours = 14, minutes = 0), None)
s8 = Student('Marta', 'Biss', timedelta(minutes = 25), 0, timedelta(hours = 14, minutes = 0), None)
s9 = Student('John', 'Doe', timedelta(minutes = 25), 0, timedelta(hours = 14, minutes = 20), None)
s10 = Student('Luke', 'Ratford', timedelta(minutes = 25), 0, timedelta(hours = 16, minutes = 30), None)
s11 = Student('John', 'Snow', timedelta(minutes = 25), 0, timedelta(hours = 14, minutes = 0), None)



students = [s1, s2, s3, s5, s6, s7]        

week_days = ["Monday"]
result = { x : {} for x in week_days}
    
Student.generate_time()
print(result)

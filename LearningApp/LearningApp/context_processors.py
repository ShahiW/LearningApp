from quiz.models import Subject
from users.models import StudentClassroom

def sorted_subjects(request):
    sorted_subjects = {s.name: s for s in sorted(Subject.objects.all(), key=lambda el: el.name)}
    return {'subjects': sorted_subjects}



def available_subjects(request):
    user = request.user

    if user.is_authenticated:
        classrooms = StudentClassroom.objects.filter(student=user)

        if classrooms:
            student_year = classrooms[0].classroom.class_number
            return {'subjects': Subject.objects.filter(year=student_year)}
        else:
            return {"subjects": Subject.objects.all()}
        
    else: 
        return {'subjects': []}

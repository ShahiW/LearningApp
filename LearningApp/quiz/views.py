from django.shortcuts import render
from .models import Category, Subject, Question, Answer, Score
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection  # zeigt queries genauer und wie schnell performed
from django.db.models import Q  # Keyword argument queries


def home(request):
    return render(request, "quiz/base.html")


def about(request):
    return render(request, "quiz/about.html")


@login_required
def categories(request, subject: str):
    if Subject.objects.filter(name__iexact=subject).exists():
        context = {
            "categories": Category.objects.filter(
                subject__name__iexact=subject
            ),  # iexact um upper-lower-case zu ignorieren
            "subject": subject,
        }

        return render(request, "quiz/category.html", context)

    else:
        raise Http404("Ooops! Diese Seite existiert leider nicht.")
    

@login_required
def quiz(request, c_id):
    user = request.user
    question = Question.objects.filter(category__id=c_id).first()
    if question:
        context = {
            "category": Category.objects.get(id=c_id),
            "question": question,
            "answers": Answer.objects.filter(question__id=question.id),
        }

        return render(request, "quiz/quiz.html", context)
    else:
        raise Http404("Ooops! Diese Frage existiert leider nicht.")

    # else:
    messages.info(
        request,
        f"Toll { user.username }! Du hast das Quiz beendet. Dein Punktestand ist: <score>",
    )


@login_required
def check_answer(request, a_id):
    answer = Answer.objects.get(id=a_id)
    question = answer.question
    right_answer = Answer.objects.get(is_correct=True, question=question)
    category = question.category
    subject = category.subject
    user = request.user

    if answer.is_correct:
        score = Score(
            user = user,
            subject = subject,
            category = category,
            question = question,
            value = question.marks,
        )
        score.save()
    
    else:
        messages.info(request, f"Leider falsch. Die richtige Antwort ist { right_answer }")
        score = Score(
            user = request.user,
            subject = subject,
            category = category,
            question = question,
            value = 0,
        )
        score.save()

    return quiz(request, category.id)


###############
# ORM Tutorial
###############

# OR QUERIES
####################################################################################

#def show_questions_(request):
    #questions = Question.objects.all()

    #print(questions)  zeigt sql code im terminal
    #print(questions.query)  zeigt performance der query
    #print(connection.queries)

    #return render(request, "quiz/about.html", {'questions': questions})

# Simple OR Query
#def show_questions_(request):
        #questions = Question.objects.filter(marks=1) | Question.objects.filter(question__startswith=48)

        #print(questions)
        #print(connection.queries)

        #return render(request, "quiz/about.html", {"questions": questions})

# Q objects: 
def show___questions_(request):
    questions = Question.objects.filter(Q(marks=1) 
                                        | Q(question__startswith=48) 
                                        | ~Q(marks=2))  # not mark

    print(questions)
    print(connection.queries)

    return render(request, "quiz/about.html", {"questions": questions})

    
# Simple AND QUERIES
####################################################################################
def show_questions___(request):
    # anstelle von fragen, jetzt mal antworten
    # Gib mir alle Antworten aus meiner DB, die nicht korrekt sind und mit einer 6 beginnen:
    answers = Answer.objects.exclude(is_correct=True) & Answer.objects.filter(answer__startswith=6)

    print(answers)
    print(connection.queries)

    return render(request, "quiz/about.html", {"answers": answers})


def show_questions__(request):
    # anstelle von fragen, jetzt mal antworten
    # Gib mir alle Antworten aus meiner DB, die korrekt sind und mit einer 6 beginnen:
    answers = Answer.objects.filter(Q(is_correct=True) & Q(answer__startswith=6))

    print(answers)
    print(connection.queries)

    return render(request, "quiz/about.html", {"answers": answers})


# Simple UNION QUERIES
# Returns all items from selected tables, but only the uniques! UNION removes any duplicate rows.
# -> Der UNION-Operator wählt standardmäßig nur eindeutige Werte aus. Um doppelte Werte zuzulassen, verwenden Sie das Argument all=True
# Union can only be used on tables with the same fields and datatypes.
####################################################################################


def show_questions____(request):
    questions = (
        Answer.objects.all()
        #.values_list("answer")
        .values('answer')
        .union(Question.objects.all()
        #.values_list("question"))
        .values('question'))
    )

    print(questions)
    print(connection.queries)

    return render(request, "quiz/about.html", {"questions": questions})

# Database can return data in three different ways: as objects, as dictionairies and as tuples.
# "values_list" returns tuples, "values" returns a dictionairy


# Simple NOT QUERIES
# NOT example: 
# SELECT * FROM Students WHERE NOT Age = 21
# exclude(<condition>)
# filter(~Q(<condition>))
####################################################################################

# Simple EXCLUDE
def show__questions(request):
    #answers = Answer.objects.exclude(answer=60)
    answers = Answer.objects.exclude(answer__gt=20)

    # Opertoren, die man verwenden kann:
    # = gleich
    # != nicht gleich
    # > größer als
    # < kleiner als
    # >= größer als oder gleich
    # <= kleiner als oder gleich

    # oder diese hier: django docs:https://docs.djangoproject.com/en/5.0/ref/models/querysets/#gt
    # gt, lt, gte, lte, startswith, in...

    print(answers)
    print(connection.queries)

    return render(request, "quiz/about.html", {"answers": answers})

# Simple NOT ~Q()
def show__questions_(request):
    answers = Answer.objects.filter(~Q(answer__gt=20)&~Q(is_correct=True))

    print(answers)
    print(connection.queries)

    return render(request, "quiz/about.html", {"answers": answers})


# Simple Field Select Output
# Selecting individual database fields
# Outputting to template
####################################################################################

# Select and output individual fields
def show_questions_(request):
    answers = Answer.objects.filter(is_correct=True).only('answer', 'updated_at')  # mit .only kann man sich spezifische felder anzeigen lassen

    print(answers)
    print(connection.queries)

    return render(request, "quiz/about.html", {"answers": answers})


# simple PERFORMING RAW QUERIES 
####################################################################################

def show_questions(request):
    # answers = Answer.objects.all()

    answers = Answer.objects.raw('select * from quiz_answer where is_correct=True')

    print(answers)
    print(connection.queries)

    return render(request, "quiz/about.html", {"answers": answers})
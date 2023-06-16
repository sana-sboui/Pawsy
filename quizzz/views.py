from django.shortcuts import render
from .models import Quiz
from .models import Question
from .models import Answer
from django.http import JsonResponse
from rslts.models import Result







def quiz_data(request, quiz_name):
    if request.method == "GET":
        quiz = Quiz.objects.get(name = quiz_name)
        questions=[]
        for q in quiz.get_questions():
            answers=[]
            for a in q.get_answers():
                answers.append(a.text)
            questions.append({str(q): answers})
        return JsonResponse({
            'data':questions,
            'time':quiz.time,
        })
    elif request.method == "POST":
        
        questions=[]
        
        data= request.POST

        data_=dict(data.lists())
        
        data_.pop('csrfmiddlewaretoken')
        
        for k in data_.keys():
            
            question=Question.objects.get(text=k)
            questions.append(question)
        
        user=request.user
        quiz=Quiz.objects.get(name=quiz_name)


        score=0
        multiplier=100/quiz.number_of_questions
        results=[]
        correct_answer= None


        for q in questions:
            a_selected=request.POST.get(q.text)
            if a_selected !="":
                question_answers=Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected==a.text:
                        if a.correct:
                            score+=1
                            correct_answer=a.text
                    else:
                        if a.correct:
                            correct_answer=a.text
                results.append({str(q): {'correct_answer':correct_answer, 'answered':a_selected}})  
            else:
                results.append({str(q):'Question non résolue'})   

        score_=score*multiplier   
        Result.objects.create(quiz=quiz, user=user, score=score_)  

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed':True, 'score':score_ , 'results':results})
        else:
            return JsonResponse({'passed': False, 'score':score_ , 'results':results})




    





def quiz_list(request):
    quizzes = Quiz.objects.all()
    context = {'quizzes': quizzes}
    return render(request, 'quiz_list.html', context)

def quiz_detail(request, quiz_name):
    try:
        quiz = Quiz.objects.get(name=quiz_name)
    except Quiz.DoesNotExist:
        return render(request, '404.html')
    questions = Question.objects.filter(quiz__in=[quiz])
    answers = Answer.objects.filter(question__in=questions)
    context = {'questions': questions, 'answers': answers, 'quiz': quiz}
    return render(request, 'quiz_detail.html', context)
    


# Create your views here.
"""def quizz(request):
    if request.method == "POST":
        name = request.POST['name']
        topic = request.POST['topic']
        number_of_questions = request.POST['number_of_questions']
        time = request.POST['time']
        required_score_to_pass = request.POST['required_score_to_pass']
 
        
        return render(request,"base.html", {      'name': name,
                                                    'topic': topic,
                                                    'number_of_questions': number_of_questions,
                                                    'time': time,
                                                    'required_score_to_pass': required_score_to_pass,})
    else:    
        return render(request,"contact.html")



from django.views.generic import ListView
class QuizListView(ListView):
    model=Quiz
    template_name= 'quizzz/main.html'
def quiz_view(request, pk):
    quiz= Quiz.objects.get(pk=pk)
    return render(request, 'quizzz/quiz.html',{'obj': quiz})

"""

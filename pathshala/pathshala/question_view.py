from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from pathshala.models import Question


def test(request):
    t = get_template('question.html')
    question = Question.objects.all()
    text = question[0].text
    options = question[0].options  
    html = t.render(Context({'text': text ,'options':options}))
    return HttpResponse(html)
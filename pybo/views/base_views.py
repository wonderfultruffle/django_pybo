from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ..models import Question

# Create your views here.
def index(request):
    page = request.GET.get("page", "1")
    kw = request.GET.get("kw", '')
    question_list = Question.objects.order_by("-create_date")
    
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | 
            Q(content__icontains=kw)| 
            Q(answer__content__icontains=kw) | 
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)).distinct()
    
    paingnator = Paginator(question_list, 10)
    page_obj = paingnator.get_page(page)
    
    context = {"question_list": page_obj, "page":page, "kw": kw}
    return render(request, "pybo/question_list.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)
    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)
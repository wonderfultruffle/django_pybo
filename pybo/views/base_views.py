from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ..models import Question

# Create your views here.
def index(request):
    page = request.GET.get("page", "1")
    print(page)
    question_list = Question.objects.order_by("-create_date")
    paingnator = Paginator(question_list, 10)
    page_obj = paingnator.get_page(page)
    context = {"question_list": page_obj}
    return render(request, "pybo/question_list.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.get(id=question_id)
    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)
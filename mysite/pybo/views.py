from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')  # - 붙이면 작성 일시 역순으로 정렬
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)  # 템플릿 파일: 파이썬 데이터를 읽어서 사용 가능한 HTML파일

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # question_id가 없을 때 서버오류(500)이 아닌 Not Found(404) 뜨도록 함
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):   # 텍스트창에 입력한 내용은 request 객체를 통해 읽을 수 있음
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())   # 답변 생성: POST로 전송된 폼 데이터 중 content값, 시간
    return redirect('pybo:detail', question_id=question.id)
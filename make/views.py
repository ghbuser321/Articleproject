from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import PhotoPost
from django.views.generic import DetailView
from django.db.models import Q
#検索のメッセジーを追加
from django.contrib import messages
from .forms import ContactForm 
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import EmailMessage






class IndexView(ListView):
    template_name = 'index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    paginate_by = 9

#ログインユーザーに限定 ログアウト状態はリダイレクト
@method_decorator(login_required, name='dispatch')
class CreateMakeView(CreateView):
    form_class = PhotoPostForm

    template_name= "makes_arti.html"
    success_url = reverse_lazy('make:makes_done')

    def form_valid(self, form):
        maksdata = form.save(commit=False)
        maksdata.user = self.request.user
        maksdata.save()
        return super().form_valid(form)

class MakeSuccessView(TemplateView):
    template_name = 'makes_success.html'

class CategoryView(ListView):
    tempalate_name = 'index.html'
    paginate_by = 9
   

    def get_queryset(self):
        category_id  = self.kwargs['category']
        categories = PhotoPost.objects.filter(category=category_id).order_by('-posted_at')
        return categories

class UserView(ListView):
    template_name ='index.html'
    paginate_by = 9

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list=PhotoPost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list

class DetailView(DetailView):
    template_name = 'detail.html'
    model = PhotoPost  

    #検索バーによるキーワード検索タイトル検索のみ
def search(request):
    query = request.GET.get('q')
    results = [] #最初に定義するのはresult

    if query:
        #検索フィルターをタイトルにする
        results = PhotoPost.objects.filter(title__icontains=query)
        messages.add_message(request, messages.INFO, f"検索ワード: {query}")

    return render(request, 'search.html', {'results': results, 'query':query})

class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = PhotoPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

#お問い合わせビュークラス
class QuestionView(FormView):
        template_name = 'question.html'
        form_class = ContactForm
        success_url = reverse_lazy('make:question')
            
        def form_valid(self, form):
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['question_title']
            message = form.cleaned_data['question_detail']
                
            subject = 'お問い合わせ：{}'.format(title)
            message = '送信者名：{0}\nメールアドレス：{1}\nタイトル：{2}\nメッセージ：{3}'.format(name, email, title, message)
                
            from_email = 'admin@example.com'
            to_list = ['admin@example.com']
                
            message = EmailMessage(subject=subject, body=message,from_email=from_email, to=to_list)
            message.send()
                
            messages.success(self.request, 'お問い合わせは正常に送信されました')
            return super().form_valid(form)

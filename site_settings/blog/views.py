from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'blog/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class UserRegister(CreateView):
    form_class = UserRegisterForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class MainView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5
    queryset = Article.objects.all().order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Whale of a Tale'
        context['reg_title'] = 'Registration'
        context['pag_href'] = '?page='
        context['form'] = CommentForm()
        context['reg_form'] = UserRegisterForm()

        return context

    def post(self, request):
        form = CommentForm(request.POST)
        reg_form = UserRegisterForm(request.POST)

        if 'text' in request.POST.keys():
            if form.is_valid():
                form.save()
                return redirect(reverse_lazy('home'))
            else:
                # wrong behavior on an invalid data. need to be fixed any time soon
                return HttpResponse('INVALID FORM DATA')

        if 'password1' in request.POST.keys():
            if reg_form.is_valid():
                reg_form.save()
                return redirect(reverse_lazy('home'))
            else:
                # wrong behavior on an invalid data. need to be fixed any time soon
                return HttpResponse('INVALID FORM DATA')

        return redirect(reverse_lazy('home'))


class NewsView(ListView):
    model = News
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    queryset = News.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Whale of a Tale - News'

        return context


class SearchView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search: ' + self.request.GET.get('q')
        context['pag_href'] = '?q=' + self.request.GET.get('q') + '&page='
        context['form'] = CommentForm()

        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Article.objects.filter(
            Q(content__icontains=query) | Q(title__icontains=query)
        )

        return object_list

    def post(self, request):
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse_lazy('search') + '?q=' + request.GET.get('q'))


class CategoryView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Whale of a Tale - ' + Category.objects.get(slug=self.kwargs['cat_slug']).name
        context['pag_href'] = '?page='
        context['form'] = CommentForm()

        return context

    def get_queryset(self):
        return Category.objects.get(slug=self.kwargs['cat_slug']).article_set.all().order_by('-id')

    def post(self, request, cat_slug=None):
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse_lazy('showByCats'))


class FeedbackFormView(CreateView):
    form_class = FeedbackForm
    template_name = 'blog/feedback.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Feedback'
        return context


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'blog/about.html', context=context)


def load_news_to_admin_panel():
    pass

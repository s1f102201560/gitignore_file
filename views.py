from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import FormClass

# Create your views here.
class Top(ListView):
  model = Post
  
  
class Detail(DetailView):
  model = Post
  
class Create(CreateView):
  model = Post
  form_class = FormClass
  new = '新規投稿'
  new_btn = '投稿'
  input_btn = 'blue-btn'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['new'] = self.new
    context['new_btn'] = self.new_btn
    context['btn'] = self.input_btn
    return context

  success_url = '/'
  
class Update(UpdateView):
  model = Post
  form_class = FormClass
  new = '更新'
  new_btn = '更新'
  input_btn = 'green-btn'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['new'] = self.new
    context['new_btn'] = self.new_btn
    context['btn'] = self.input_btn
    return context
  success_url = '/'
  
class Delete(DeleteView):
  model = Post
  
  success_url = '/'
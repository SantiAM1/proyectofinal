from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page
from .forms import PageForm


# Create your views here.

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/updatepost.html'
    success_url = reverse_lazy('pages:plataforma')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        avatar_url = usuario.avatar.url if usuario.avatar else None
        context["avatar_url"] = avatar_url
        return context
    
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/deletepost.html'
    success_url = reverse_lazy('pages:plataforma')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        avatar_url = usuario.avatar.url if usuario.avatar else None
        context["avatar_url"] = avatar_url
        return context

class ListaPages(ListView):
    model = Page
    template_name = "pages/pagelist.html"
    context_object_name = "listapages"

class ListPost(ListView):
    model = Page
    template_name = "pages/listplataforma.html"
    context_object_name = "listapages"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        nombre = usuario.first_name
        autor = nombre + " " + usuario.last_name
        ifadmin = usuario.username
        avatar_url = usuario.avatar.url if usuario.avatar else None
        context["avatar_url"] = avatar_url
        context["autor"] = autor
        context["ifadmin"] = ifadmin
        return context

class DetailPage(DetailView):
    model = Page
    template_name = "pages/detailpage.html"
    context_object_name = "page"

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/createpost.html'
    success_url = reverse_lazy('pages:plataforma')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        avatar_url = usuario.avatar.url if usuario.avatar else None
        context["avatar_url"] = avatar_url
        return context

    def form_valid(self, form):
        form.instance._autor = self.request.user
        return super().form_valid(form)

@login_required
def plataforma(request):
    usuario = request.user
    avatar_url = usuario.avatar.url if usuario.avatar else None
    print(avatar_url)
    print("-"*90)
    print(usuario.avatar)
    return render(request, "pages/inicioplataforma.html", context={"usuario": usuario, "avatar_url": avatar_url})

def about(request):
    return render(request, "pages/about.html")
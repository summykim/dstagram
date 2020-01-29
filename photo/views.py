from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy,reverse
from .models import Photo
# Create your views here.

class PhotoListView(LoginRequiredMixin,ListView):
    model = Photo
    #paginate_by = 4
    template_name = 'photo/list.html'
    context_object_name = 'photos'
    def get_queryset(self): # 컨텍스트 오버라이딩
      return Photo.objects.order_by('-updated')[:3]

class PhotoUploadView(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'

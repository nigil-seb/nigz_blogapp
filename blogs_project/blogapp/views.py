from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blogs
from .forms import Blogforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model = Blogs
    template_name = 'blogview.html'
    context_object_name = 'obj1'
class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'detail.html'
    context_object_name = 'i'
class BlogUpdateView(UpdateView):
    model = Blogs
    template_name = 'update.html'
    context_object_name = 'blog'
    fields = ('heading','desc','content','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
def blogview(request):
    obj1=Blogs.objects.all()
    if request.method=='POST':
        heading=request.POST.get('heading')
        desc=request.POST.get('desc')
        content=request.POST.get('content')
        date=request.POST.get('date')
        obj=Blogs(heading=heading,desc=desc,content=content,date=date)
        obj.save()
    return render(request,'blogview.html',{'obj1':obj1})
def delete(request,blogid):
    blog=Blogs.objects.get(id=blogid)
    if request.method=='POST':
        blog.delete()
        return redirect('/')
    return render(request,'delete.html',{'blog':blog})
def update(request,id):
    blog=Blogs.objects.get(id=id)
    form=Blogforms(request.POST or None,instance=blog)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'blog':blog,'form':form})
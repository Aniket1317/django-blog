from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404

from .forms import MyBlogForm, MyBlogModelForm
from .models import MyBlog

# Create your views here.

# def blog_post_details_page(request,slug):
# 	# queryset= MyBlog.objects.filter(slug= slug)
# 	# if queryset.count() == 0:
# 	# 	raise Http404
# 	# else:
# 	# 	obj = queryset.first()
# 	obj = get_object_or_404(MyBlog, slug= slug)
# 	template_name = 'blog_post_details.html'
# 	context = {"object" : obj}
# 	return render(request, template_name, context)




#CRUD

def blog_post_list_view(request):
	qs= MyBlog.objects.all().published()
	if request.user.is_authenticated:
		my_qs = MyBlog.objects.filter(user= request.user)
		qs = (qs | my_qs).distinct()
	template_name = 'blog/list.html'
	context = {"object_list" : qs}
	return render(request, template_name, context)



# @login_required
@staff_member_required
def blog_post_create_view(request):
	form = MyBlogModelForm(request.POST or None)
	if form.is_valid():
		# obj = MyBlog.objects.create(**form.cleaned_data)
		obj= form.save(commit=False)
		obj.user = request.user
		obj.save()
		form = MyBlogModelForm()
	template_name = 'form.html'
	context = {"form" : form}
	return render(request, template_name, context)




def blog_post_details_view(request, slug):
	obj = get_object_or_404(MyBlog, slug= slug)
	template_name = 'blog/details.html'
	context = {"object" : obj}
	return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
	obj = get_object_or_404(MyBlog, slug= slug)
	form = MyBlogModelForm(request.POST or None, instance= obj)
	if form.is_valid():
		form.save()
	template_name = 'form.html'
	context = {"title" : f"Update {obj.title}", "form" : form}
	return render(request, template_name, context)



@staff_member_required
def blog_post_delete_view(request, slug):
	obj = get_object_or_404(MyBlog, slug= slug)
	template_name = 'blog/delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect('/blog')
	context = {"object" : obj}
	return render(request, template_name, context)
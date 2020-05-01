from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import MyBlog

def home_page(request):
    my_title = "Hello there...."
    qs = MyBlog.objects.all()[:5]
    context = {"title": "Welcome to My Blog", 'blog_list': qs}
    return render(request, "home.html", context)

def about_page(request):

	return render(request, "about.html", {"title": "about"})

def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context={
		"title" : "Contact Us",
		"form" : form
	}
	return render(request, "form.html", context)




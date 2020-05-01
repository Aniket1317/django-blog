from django import forms

from .models import MyBlog


class MyBlogForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget= forms.Textarea)


class MyBlogModelForm(forms.ModelForm):
	class Meta:
		model = MyBlog
		fields = ['title', 'slug', 'content', 'publish_date']


	def clean_title(self, *args, **kwargs):
		instance = self.instance
		title= self.cleaned_data.get("title")
		print(title)
		qs= MyBlog.objects.filter(title__iexact= title)
		if instance is not None:
			qs = qs.exclude(pk= instance.pk) #id=instance.id(for updating with same title)
		if qs.exists():
			raise forms.ValidationError("This title already exist") #(for not creating with used title)
		return title
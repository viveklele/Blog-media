from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.db.models import Q
from django.http import JsonResponse

def home(request):
	context = {
	    'posts': Post.objects.all()
	}
	# posts = Post.objects.all()
	# return render(request, 'blog/home.html', posts)
	
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # '<app>/<model>_<viewtype>.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html' # '<app>/<model>_<viewtype>.html'
	context_object_name = 'posts'
	paginate_by = 5
	
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('date_posted')
		
		
class PostDetailView(DetailView):
	model = Post
	
	
class PostCreateView(LoginRequiredMixin, CreateView): 
	model = Post
	
	fields = ['title', 'content', 'blog_image', 'audio', 'video', 'keywords']
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
	model = Post
	fields = ['title', 'content', 'blog_image', 'audio', 'video', 'keywords']
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

	
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostGridView(ListView):
	model = Post
	template_name = 'blog/gridview.html' # '<app>/<model>_<viewtype>.html'
	context_object_name = 'posts'
	paginate_by = 6

def grid_view(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/gridview.html', context)

# return search query

def search(request):
	query = request.GET['query']

	if len(query) > 20:
		allPosts = Post.objects.none()
		user = Profile.objects.none()
	else:
		allPosts = Post.objects.filter(Q(title__icontains=query) | Q(author__username__icontains=query) | 
		Q(keywords__icontains=query))

	paras = {
		'allPosts': allPosts, 'query': query
	}
	
	return render(request, 'blog/search.html', paras)

# show suggetions in search bar

# def search_address(request):
# 	title = request.GET.get('title')
# 	payload = []
# 	if title:
# 		fake_address_objs = Post.objects.filter(Q(author__username__icontains=title))
# 		# fake_address_objs = Post.objects.filter(Q(author__username__icontains=title) | Q(title__icontains=title) |
#  		# Q(keywords__icontains=title))

# 		for fake_address_obj in fake_address_objs:
# 			payload.append(fake_address_obj.title)
	
# 	return JsonResponse({
# 		'status': 200,
# 		'data': payload
# 	})
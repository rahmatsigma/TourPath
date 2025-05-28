from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post, UserProfile
from django.http import JsonResponse

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/registrasi.html', {'form': form})

@login_required
def index(request):
    return render(request, 'blog/index.html')

@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def settings_view(request):
    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        bio = request.POST.get('bio')
        profile.bio = bio
        profile.save()
        return JsonResponse({'status': 'success'})
    
    context = {
        'user_profile': profile
    }
    return render(request, 'blog/setting.html', context)

@login_required
def rencana_view(request):
    return render(request, 'blog/rencana.html')

@login_required
def about_view(request):
    return render(request, 'blog/about.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('login')
    return redirect('settings')

@login_required
def destinasi_view(request):
    return render(request, 'blog/destinasi.html')
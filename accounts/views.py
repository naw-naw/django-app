from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.http import HttpResponse


def register_view(request):  #@hello_user, makoi123
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		user_obj = form.save()
		return redirect('/login')
	context = {"form": form}
	return render(request, "accounts/register.html", context)


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/')
	else:
		form = AuthenticationForm(request)
	# without context, validation error not showing
	context ={
		"form": form
	}
	return render(request, "accounts/login.html", context)

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect("/login/")
	return render(request, "accounts/logout.html", {})



"""
def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password) #if doesn't match return None, or return user
		if user is None:
			context = {"error": "Invalid username and password"}	
			return render(request, "accounts/login.html", context)
		login(request, user)
		return redirect('/')
	return render(request, "accounts/login.html", {})

"""
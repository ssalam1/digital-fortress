from player.forms import registrationForm
from hunt import settings
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django import forms
from player.models import userInfo
from level.models import level
from fandjango.decorators import facebook_authorization_required


def index(request):
	if request.facebook:
		ui = userInfo.objects.filter(user = request.facebook.user)
		if len(ui):
			try:
				redirect_level = level.objects.get(number = ui[0].max_level)
			except:
				return HttpResponse('Adding More Levels. Stay Tuned')
			return HttpResponseRedirect('/level/'+redirect_level.slug)
	
		return render_to_response('index.html', {} , context_instance=RequestContext(request))
	else:
		return render_to_response('index.html', {} , context_instance=RequestContext(request))

def privacy_policy(request):
	return render_to_response('policy.html', {} , context_instance=RequestContext(request)) 

@facebook_authorization_required
def authorize(request):
	ui = userInfo.objects.filter(user = request.facebook.user)
	if len(ui):
		redirect_level = level.objects.get(number = ui[0].max_level)
		return HttpResponseRedirect('/level/'+redirect_level.slug)
	else:
		try:
			user_info = userInfo(user = request.facebook.user, email = request.facebook.user.email, college = "N/A" ,max_level = 1)
			user_info.save()
		except:
			user_info = userInfo(user = request.facebook.user, email = "notavalable@abc.in", college = "N/A" ,max_level = 1)
			user_info.save()
		redirect_level = level.objects.get(number = 1)
		return HttpResponseRedirect('/level/'+redirect_level.slug)

"""def account_handler(request):
	if request.method == 'POST':
		form = registrationForm(request.POST)
		if form.is_valid():
			college = form.cleaned_data['college']
			email = form.cleaned_data['email']
			user_info = userInfo(user = request.facebook.user, email = email, college = college ,max_level = 1)
			user_info.save()
			redirect_level = level.objects.get(number = 1)
			return HttpResponseRedirect('/level/'+redirect_level.slug)
		else:
			return HttpResponse(form.errors)
	else:
		return HttpResponseRedirect('/')
	

	

def index(request):
	if request.user.username:
		#change
		if request.user.username != 'shouvik':
			ui = userInfo.objects.get(user = request.user)
			redirect_level = level.objects.get(number = ui.max_level)
			return HttpResponseRedirect('/level/'+redirect_level.slug)
	form1 = loginForm
	form2 = registrationForm
	return render_to_response('index.html', {'login_form':form1,'registration_form':form2} , context_instance=RequestContext(request))
	
@facebook_authorization_required
def checklogin(request):
	form = loginForm(request.POST)	
	if form.is_valid():
		user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
	else:
		return HttpResponse('Form has errors')
	if user is not None:
		if user.is_active:
			login(request, user)
			ui = userInfo.objects.get(user = user)
			redirect_level = level.objects.get(number = ui.max_level)
			return HttpResponseRedirect('/level/'+redirect_level.slug)
        	
	else:
		return HttpResponse('No login')
	
@facebook_authorization_required
def checkreg(request):
	if request.method == 'POST':
		form = registrationForm(request.POST)
		if form.is_valid():
			first_name = request.facebook.user.first_name
			last_name = request.facebook.user.last_name
			college = form.cleaned_data['college']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = request.facebook.user.email
			full_name = first_name + last_name
			u = User.objects.create_user(username, email, password)
			u.is_active = True 
			u.save()
			user_info = userInfo(user = u, name = full_name, college = college ,max_level = 1)
			user_info.save()
					
		return HttpResponse(form.errors)
	else:
		return HttpResponse('Shit Happened')"""


def log_out(request):
	request.facebook = None
	return HttpResponseRedirect('/')

from django.shortcuts import render
from django.template import loader
from django.core.mail import send_mail
from .models import ServiceDetail, BlogPost

# Create your views here.

def home(request) :
	return render(request, 'home.html', {})

def about(request) :
	return render(request, 'about.html', {})

def contact(request) :
	# determine what request is being received
	if request.method == "POST":
		email = request.POST['message-email']
		name = request.POST['message-name']
		content = request.POST['message']

		message = f"Sent By: {name} \n email: {email} \n content:{content}"
	
		# send email
		'''
		send_mail(subject=name,
			message=message,
			from_email='lesjameswilson@gmail.com',
			recipient_list=[email],
			fail_silently=False)
		'''
		return render(request, 'contact.html', {'message_name' : name})
		
	else:
		#
		# 	
		return render(request, 'contact.html', {})

def pricing(request) :
	services = ServiceDetail.objects.all().values()
	return render(request, 'pricing.html', context = { 'services': services, })

def service(request) :
	return render(request, 'service.html', {})

def blog(request) :
	blogs = BlogPost.objects.all().values()
	return render(request, 'blog.html', context = {"blogs":blogs})

def blog_details(request, id) :
	blog_post = BlogPost.objects.get(id = id)
	return render(request, 'blog-details.html', context ={"blog_post":blog_post})

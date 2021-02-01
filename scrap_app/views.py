from django.shortcuts import render,redirect,get_object_or_404
from .models import User,Project
from .form import EmployeeUserForm,EmployeeProjectForm
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.

class EmployeeRegisterView(generic.View):
	model = User
	form_class = EmployeeUserForm
	template_name = 'employes/emp_register.html'

	def post(self,request):
		form = EmployeeUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		return render(request,self.template_name,{'form':form})

	def get(self,request):
		form = self.form_class()
		return render(request,self.template_name,{'form': form})

class ProjectRegisterView(generic.View):
	model = Project
	form_class = EmployeeProjectForm
	template_name = 'projects/project.html'

	def post(self,request):
		if request.user.is_authenticated:
			form = EmployeeProjectForm(request.POST)
			if form.is_valid():
				user=form.save(commit=False)
				user.employee = request.user
				user.save()
				return HttpResponse("Your response is submitted")
			return render(request,self.template_name,{'form':form})
		return redirect('register') 			

	def get(self,request):
		form = self.form_class()
		return render(request,self.template_name,{'form': form})

class ProjectDetailView(generic.ListView):
	template_name = 'projects/project_detail.html'
	content_object_name = 'project_list'

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Project.objects.all()
		return Project.objects.filter(pk=self.request.user.id)	



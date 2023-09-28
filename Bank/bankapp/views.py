from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .forms import BranchForm
from .models import District,Branch


# Create your views here.
def index(request):
    return render(request,'Home.html')
def simple(request):
    return render(request,'new.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/new')
        else:
            messages.info(request,"Invalid User")
            return redirect('/login')
    return render(request,"login.html")
def reg(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cnf_password=request.POST['cnfpassword']
        if password==cnf_password:
            if User.objects.filter(username=username).exists():
                # this is to display on webpage "Already User exists"
                messages.info(request,"Already User exists")
                # goes to register page itself by giving urls.py name
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                messages.info(request, "Successfully Registered")
                # this would print the message on terminal
                print("User Created")
                # goes to home page
                return redirect('/login')
        else:
            messages.info(request, "Password does not match")
            print("Password does not match")
    return render(request,"register.html")

def form(request):
    form = BranchForm(request.GET)
    return render(request, 'form.html', {'form': form})

from django.http import JsonResponse
from .models import Branch

def get_filtered_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id)
    branch_choices = [(branch.id, branch.name) for branch in branches]
    return JsonResponse({'branch_choices': branch_choices})

class BranchView(View):
    template_name = 'form.html'

    def get(self, request):
        form = BranchForm()
        messages.success(request, "Application Received")
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BranchForm(request.POST)
        messages.success(request, "Application Received")
        return render(request, self.template_name, {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')
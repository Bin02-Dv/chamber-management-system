from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *

# Create your views here.

def logout(request):
    auth.logout(request)
    return render(request, "logout.html")

def signUp(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exist!!')
            return redirect('signUp')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username aleady exist !!')
            return redirect('signUp')
        elif confirmPassword != password:
            messages.error(request, 'password and confirm password missed match !!')
            return redirect('signUp')
        else:
            new_user = User.objects.create_user(username=username, password=password, email=email)
            new_user.save()

            user_model = User.objects.get(username=username)
            new_signUp = SignUp.objects.create(user=user_model, fullname=fullname, id_user=user_model.id)
            new_signUp.save()
            messages.success(request, 'Sign up completed successful....')
            return redirect('login')
    return render(request, 'sign-up.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successful.....')
            return redirect('user-dashboard')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')
    return render(request, 'login.html')

def user_dashboard(request):
    user = User.objects.get(username=request.user)
    return render(request, 'user-dashboard.html', {'user':user})

def scheduling(request):
    user = User.objects.get(username=request.user)
    judges = SignUp.objects.all()
    context = {
        "judges": judges,
        "user": user
    }
    if request.method == 'POST':
        case_title = request.POST['caseTitle']
        case_date = request.POST['date']
        case_time = request.POST['time']
        judge = request.POST['judge']

        new_case = Scheduling.objects.create(
            case_title=case_title, case_date=case_date, case_time=case_time,
            judged=judge, case_status=False
        )
        new_case.save()
        case_num = Scheduling.objects.get(case_title=case_title)
        case_num.case_number = f"CN-{case_num.id}"
        case_num.save()
        messages.success(request, 'Case added successfully...')
        return redirect('scheduling')
    return render(request, 'scheduling.html', context)

def manage_case(request):
    cases = Scheduling.objects.all()
    user = User.objects.get(username=request.user)
    context = {
        "cases":cases,
        "user": user
    }
    return render(request, 'case-management.html', context)

def manage_case2(request):
    user = User.objects.get(username=request.user)
    jud = SignUp.objects.filter(user=user)
    fullname = ''
    for name in jud:
        fullname = f"Judge {name.fullname}"

    cases2 = Scheduling.objects.filter(judged=fullname)
    context = {
        "case":cases2,
        "user": user
    }
    return render(request, 'case-management.html', context)

def case_view(request, id):
    user = User.objects.get(username=request.user)
    cases = Scheduling.objects.get(id=id)
    documents = DocumentManagement.objects.filter(doc_id=id)
    context = {
        "case":cases,
        "documents": documents,
        "user": user
    }
    return render(request, 'case-view.html', context)

def document_upload(request, id):
    user = User.objects.get(username=request.user)
    cases = Scheduling.objects.get(id=id)
    documents = DocumentManagement.objects.filter(doc_id=cases.id)
    context = {
        "case":cases,
        "documents": documents,
        "user": user
    }
    if request.method == 'POST':
        if request.FILES.get("uploadDocument") != None:
            document = request.FILES.get("uploadDocument")
            case_doc = DocumentManagement.objects.create(doc_number=cases, doc_id=cases.id, document=document)
            case_doc.save()
            cases.case_status = True
            cases.save()
            messages.success(request, "Document Uploaded Successfully...")
            return redirect("/document-upload/"+str(id))
        else:
            messages.error(request, "Sorry You did not upload anything, please upload a document!!")
            return redirect("/document-upload/"+str(id))
    return render(request, 'document-management.html', context)

def profile(request):
    c_user = User.objects.get(username=request.user)
    user = SignUp.objects.get(user=request.user)
    context = {
        "user": user,
        "cuser": c_user
    }
    if request.method == 'POST':
        fullname = request.POST['fullname']
        phone = request.POST['phone']

        user.fullname = fullname
        user.phone_number = phone
        user.save()
        messages.success(request, "Profile updated successfully...")
        return redirect("profile")
    return render(request, "user-profile.html", context)

def settings(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if cpassword == password:
            user.set_password(password)
            user.save()
            messages.success(request, "login details update successful...")
            return redirect("login")
        else:
            messages.error(request, "password and confirm password missed matched!")
            return redirect("settings")
    return render(request, "settings.html", {"user":user})

def support(request):
    return render(request, "support.html")

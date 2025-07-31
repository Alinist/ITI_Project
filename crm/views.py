from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q
from crm.forms import CreateRecordForm, CreateUserForm, LoginForm, UpdateRecordForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


from crm.models import Record


def home(request):
    return render(request, 'pages/index.html')

def add_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'User created successfully.')
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'pages/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f'Welcome {user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission.')

    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'form': form})

@login_required(login_url='login')
def Logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    return render(request, 'pages/dashboard.html', {'records': records})

@login_required(login_url='login')
def add_record(request):
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record added successfully.')
            return redirect('dashboard')
    else:
        form = CreateRecordForm()
    return render(request, 'pages/add_record.html', {'form': form})

@login_required(login_url='login')
def view_record(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'pages/view_record.html', {'record': record})

@login_required(login_url='login')
def edit_record(request, record_id):
    record = Record.objects.get(id=record_id)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Record updated successfully.')
            return redirect('dashboard')
    else:
        form = UpdateRecordForm(instance=record)
    return render(request, 'pages/edit_record.html', {'form': form, 'record': record})

@login_required(login_url='login')
def delete_record(request, record_id):
    record = Record.objects.get(id=record_id)
    record.delete()
    messages.error(request, 'Record deleted successfully.')
    return redirect('dashboard')

@login_required(login_url='login')
def search(request):
    query = request.GET.get('q')
    records = Record.objects.all()
    if query:
        terms = query.split()
        if len(terms) == 1:
            records = records.filter(
                Q(first_name__icontains=terms[0]) |
                Q(last_name__icontains=terms[0])
            )

        elif len(terms) >= 2:
            first_term = terms[0]
            last_term = terms[1]

            records = records.filter(
                Q(first_name__istartswith=first_term) &
                Q(last_name__istartswith=last_term)
            ) | records.filter(
                Q(first_name__icontains=first_term) &
                Q(last_name__icontains=last_term)
            )
    else:
        records = Record.objects.all()
    return render(request, 'pages/dashboard.html', {'records': records, 'query': query})

def error(request, exception):
    return render(request, 'pages/error.html')
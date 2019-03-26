from django.shortcuts import render
from expenses.forms import ExpenseForm
from expenses.models import Expenses
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@login_required(login_url='signin')
@csrf_protect
def dashboard(request):
    msg = ''
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expenses = Expenses()
            expenses.client = request.user
            expenses.title = form.cleaned_data['title']
            expenses.description = form.cleaned_data['description']
            expenses.amount = form.cleaned_data['amount']
            expenses.currency = form.cleaned_data['currency']
            expenses.date = form.cleaned_data['date']
            expenses.save()
            form = ExpenseForm()
            msg = 'Expense added successfully'
    return render(request, 'dashboard.html', {'form': form, 'msg': msg})


@login_required(login_url='signin')
@csrf_protect
def read(request):
    data = Expenses.objects.filter(client_id=request.user.id)
    return render(request, 'expenselist.html', {'data': data})


@login_required(login_url='signin')
@csrf_protect
def viewall(request):
    data = Expenses.objects.all()
    return render(request, 'viewall.html', {'data': data})


def viewrow(request):
    resultset = Expenses.objects.get(id=request.GET['id'])
    return render(request, 'viewrow.html', {'data': resultset})
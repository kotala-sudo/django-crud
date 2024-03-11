from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Employee
from .forms import AddEmployeeForm


# Create your views here.
def home(request):
    # retrieving employee records from database
    employee_list = Employee.objects.all()
    return render(request, "website/home.html", {"emp_list": employee_list})


def login_user(request):
    # if the method is POST
    if request.method == "POST":
        # retrieve the values of username and password passed from login.html
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate the user
        user = authenticate(username=username, password=password)

        # if user object is not none meaning successfully authenticated
        if user is not None:
            # if authentication is successful login the user, display a message and redirct to home.
            login(request, user)
            messages.success(
                request, "You have been authenticated and successfully logged in."
            )
            return redirect("home")
        else:
            # if authentication is unsuccessful display a message and redirct to login page.
            messages.success(
                request, "Sorry authentication failed and your login was unsuccessful."
            )
            return redirect("login")
    else:
        return render(request, "website/home.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect("home")


def employee_view(request, pk):
    if request.user.is_authenticated:
        employee = Employee.objects.get(emp_id=pk)
        return render(request, "website/employee.html", context={"emp": employee})
    else:
        messages.success(request, "You must be logged in to view the employee records")
        return redirect("home")


def delete_employee(request, pk):
    if request.user.is_authenticated:
        employee = Employee.objects.get(emp_id=pk)
        employee.delete()
        messages.success(request, "Employee record was deleted successfully.")
        return redirect("home")
    else:
        messages.success(request, "You must be logged in to delete the employee record")
        return redirect("home")


def add_employee(request):
    # retrieving the form data
    form = AddEmployeeForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                new_employee = form.save()
                messages.success(
                    request, "A new employee record was added successfully."
                )
                return redirect("home")
        return render(request, "website/add_employee.html", {"form": form})
    else:
        messages.success(request, "You must be logged in")
        return redirect("home")


def update_employee(request, pk):
    # retrieving the employee that is being updated using primary key
    current_employee = Employee.objects.get(emp_id=pk)
    # retrieving the form entries with the updated field values
    # passing an instance of record to form
    form = AddEmployeeForm(request.POST or None, instance=current_employee)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(
                    request, "A current employee record was updated successfully."
                )
                return redirect("home")
        return render(request, "website/update_employee.html", {"form": form})
    else:
        messages.success(request, "You must be logged in")
        return redirect("home")

from django.shortcuts import render, redirect
from .forms import BasicCalculatorForm, AdvancedCalculatorForm

def basic_calculator_view(request):
    form = BasicCalculatorForm(request.POST or None)
    result = None

    if request.method == 'POST' and form.is_valid():
        num1 = form.cleaned_data['num1']
        num2 = form.cleaned_data['num2']
        operation = form.cleaned_data['operation']
        result = calculate_basic_result(num1, num2, operation)

    return render(request, 'calci/basic_calculator.html', {'form': form, 'result': result})


def calculate_basic_result(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Cannot divide by zero'
    else:
        return 'Error: Invalid operation'


def advanced_calculator_view(request):
    form = AdvancedCalculatorForm(request.POST or None)
    result = None

    if request.method == 'POST' and form.is_valid():
        num1 = form.cleaned_data['num1']
        num2 = form.cleaned_data['num2']
        operation = form.cleaned_data['operation']
        result = calculate_advanced_result(num1, num2, operation)

    return render(request, 'calci/advanced_calculator.html', {'form': form, 'result': result})


def calculate_advanced_result(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Cannot divide by zero'
    elif operation == 'square_root':
        return num1 ** 0.5
    elif operation == 'exponent':
        return num1 ** num2
    else:
        return 'Error: Invalid operation'

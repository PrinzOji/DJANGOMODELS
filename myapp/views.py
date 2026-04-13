from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def contacts(request):
    return render(request, 'contacts.html')

def contact2(request):
    context = {}
    form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            context['success_message'] = "Form submitted successfully!"
        else:
            context['error_message'] = "There was an error submitting the form. Please check the details and try again."

    context['form'] = form

    return render(request, 'contact2.html', context)
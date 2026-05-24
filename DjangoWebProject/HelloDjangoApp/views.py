from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def contact(request):
    return render(request, 'HelloDjangoApp/Contact.html')

def about(request):
    return render(request, 'HelloDjangoApp/About.html')

def index(request):
    return render(request, 'HelloDjangoApp/Index.html') 

def generate_outline(request):
    outline = None
    uploaded_file_name = None
    
    if request.method == 'POST':
        outline = {
            'unit_name': request.POST.get('unitName'),
            'unit_code': request.POST.get('unitCode'),
            'unit_description': request.POST.get('unitDescription'),
            'unit_url': request.POST.get('unitUrl'),
        }
        
        if 'document' in request.FILES:
            uploaded_file = request.FILES['document']
            uploaded_file_name = uploaded_file.name

    return render(request, 'HelloDjangoApp/Index.html', {
        'outline': outline, 
        'file_name': uploaded_file_name
    })
def assessments(request):
    assessment_list = [
        {'title': 'First IT project', 'date': '2026-06-15', 'weight': '30%'},
        {'title': 'The Prototype', 'date': '2026-07-01', 'weight': '30%'},
        {'title': 'Final project', 'date': '2026-07-10', 'weight': '40%'},
    ]
     
    return render(request, 'Assessments.html', {'assessments': assessment_list})

def contact(request):
    return render(request, 'HelloDjangoApp/Contact.html')
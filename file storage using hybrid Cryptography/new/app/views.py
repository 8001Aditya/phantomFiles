from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import User, FileUpload
import os

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # Handle registration logic
        return JsonResponse({'message': 'Registration successful.'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            return JsonResponse({'message': 'Login successful.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'Invalid username or password.'})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        # Handle file upload logic
        return JsonResponse({'message': 'File uploaded successfully.'})

def download(request, filename):
    file_upload = get_object_or_404(FileUpload, file=filename)
    file_path = file_upload.file.path
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response

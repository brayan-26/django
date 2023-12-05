from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm as formulario
from django.contrib.auth.models import User

# Create your views here.
def main(request):
    titulo = 'todo melo'
    mensaje = 'esto es un mensaje de vista'
    
    if request.method == 'GET':
        return render(request, 'main.html', {
            'titulo' : titulo, 
            'mensaje' : mensaje,
            'form' : formulario, 
        })
    else:
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            message = 'las contraseñas coinciden "melo"'
            user = User.objects.create_usser(
                username = request.POST['username'],password= request.POST['password1']
            )
            user.save()
            return render(request, 'main.html', {
                'mensaje' : message,
                'form' : formulario, 
            })
        else:
            print("las contraseñas no coinciden")
            message = 'las contraseñas NO coinciden "paila"'
            return render(request, 'main.html', {
                'mensaje' : message,
                'form' : formulario, 
            })







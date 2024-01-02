from django.shortcuts import render, HttpResponse
from .models import Project
from django.core.mail import send_mail

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def home(request):
    # Lógica de la página de inicio
    return render(request, 'home.html')

def profile(request):
    # Lógica de la página de perfil
    return render(request, 'profile.html')

def contact(request):
    # Lógica de la página de contacto
    return render(request, 'contact.html')

def enviar_correo(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        mensaje = request.POST['mensaje']

        # Verifica que todos los campos estén completos
        if nombre and correo and mensaje:
            # Personaliza el correo según tus necesidades
            subject = 'Mensaje de contacto de {}'.format(nombre)
            message = f'Nombre: {nombre}\nCorreo Electrónico: {correo}\nMensaje: {mensaje}'
            from_email = 'tu_correo@gmail.com'  # Tu dirección de correo
            recipient_list = ['salvioli.franco@gmail.com']  # Correo de destino

            # Envía el correo
            send_mail(subject, message, from_email, recipient_list)

            # Puedes redirigir a una página de confirmación
            return render(request, 'email_envio.html')
        else:
            # Algunos campos están vacíos, puedes mostrar un mensaje de error o redirigir a la página de contacto nuevamente
            return render(request, 'contact.html', {'error_message': 'Por favor, complete todos los campos.'})

    return HttpResponse('contact.html')
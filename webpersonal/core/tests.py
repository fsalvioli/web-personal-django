from django.test import TestCase
import os

email_host_password = os.environ.get('EMAIL_HOST_PASSWORD')

if email_host_password:
    print(f'Contraseña de correo: {email_host_password}')
else:
    print('La variable de entorno EMAIL_HOST_PASSWORD no está configurada.')

# El código anterior imprimirá la contraseña si está configurada en la variable de entorno.

# [System.Environment]::SetEnvironmentVariable("EMAIL_HOST_PASSWORD", "jruu qqbw jkyp zkwo", "User")


from django.shortcuts import render
from django_user_agents.utils import get_user_agent
import qrcode
from django.http import HttpResponse
from io import BytesIO

def generar_qr_apk(request):
    # URL pública de tu archivo APK
    url_apk = 'https://drive.google.com/drive/u/3/folders/1LY0F0-tJUHv7s24H0RZjKPFhTKOeIFjQ'

    # Generar el QR Code
    qr = qrcode.make(url_apk)

    # Guardar la imagen del QR en memoria
    img = BytesIO()
    qr.save(img)
    img.seek(0)

    # Devolver la imagen QR como respuesta HTTP
    return HttpResponse(img, content_type="image/png")

def mi_vista(request):
    user_agent = get_user_agent(request)
    
    if user_agent.is_mobile:
        dispositivo = 'móvil'
    elif user_agent.is_tablet:
        dispositivo = 'tablet'
    elif user_agent.is_pc:
        dispositivo = 'escritorio'
    else:
        dispositivo = 'desconocido'
    
    return render(request, 'shartter/mi_template.html', {'dispositivo': dispositivo})

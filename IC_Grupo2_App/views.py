from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

import zipfile

import os

from .modules.sad.factory import ApplicationFactory


def home(request):
    context = {
        'title': 'HomePage',
    }
    return render(request, 'IC_Grupo2_App/home.html', context)


def send(request):
    if request.method == 'GET':
        return redirect('IC_Grupo2_HomePage')

    endereco = request.POST.get('endereco')
    input_file = request.FILES['file']

    path = default_storage.save('tmp/input_file.pdf', ContentFile(input_file.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)

    highlighted_pdf, extracted_data_csv = ApplicationFactory().get_application_instance(tmp_file, endereco).run()

    zip_file = zipfile.ZipFile('tmp/retorno.zip', 'w')

    zip_file.write('tmp/highlighted.pdf')
    zip_file.write('tmp/extracted_data.csv')

    zip_file.close()

    response = HttpResponse(open('tmp/retorno.zip', 'rb'), headers={
        'Content-Type': 'application/zip',
        'Content-Disposition': 'attachment; filename="resultado.zip"',
    })

    default_storage.delete('tmp/retorno.zip')
    default_storage.delete('tmp/input_file.pdf')
    default_storage.delete('tmp/highlighted.pdf')
    default_storage.delete('tmp/extracted_data.csv')

    return response

import os
import re
from datetime import datetime
from pathlib import Path

from django.conf import settings
from django.shortcuts import render

from PIL import Image
from io import BytesIO
import base64
import pytesseract

from reader.models import ParsedImages


def read(request):
    image_data = re.sub('^data:image/.+;base64,', '', request.POST['read_image'])
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    options = "-l {}".format("por")
    result = pytesseract.image_to_string(image=image, config=options)

    print(result)

    return render(request, "home/read_result.html", {
        'result': result
    })


def save(request):
    image_data = re.sub('^data:image/.+;base64,', '', request.POST['save_image'])
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    result = request.POST['result']
    folder = request.POST['folder']
    details = request.POST['details']

    image_name = "{}.{}".format(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"), image.format)

    local_dir = os.path.join(settings.MEDIA_ROOT, folder)
    Path(local_dir).mkdir(parents=True, exist_ok=True)
    image_reference_full_path = os.path.join(local_dir, image_name)

    image.save(image_reference_full_path)

    parsed_image = ParsedImages()
    parsed_image.image = "/{}/{}".format(folder, image_name)
    parsed_image.text = result.strip().lower()
    parsed_image.text_c = result.strip().lower()
    parsed_image.details = details
    parsed_image.folder = folder
    parsed_image.save()

    return render(request, "home/save_result.html", {
        'parsed_image': parsed_image
    })

import re

from django.shortcuts import render

from PIL import Image
from io import BytesIO
import base64
import pytesseract


def read(request):

    image_data = re.sub('^data:image/.+;base64,', '', request.POST['base64'])
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    result = pytesseract.image_to_string(image=image)

    print(result)

    return render(request, "home/read_result.html", {
        'result': result
    })

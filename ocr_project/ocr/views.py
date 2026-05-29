import os
import time

import cv2
import pytesseract

from django.shortcuts import render

from .models import UploadedImage


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

os.environ["TESSDATA_PREFIX"] = (
    r"C:\Program Files\Tesseract-OCR\tessdata"
)


def apply_filter(img, filter_name):

    if filter_name == "gray":

        return cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

    elif filter_name == "threshold":

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

        _, thresh = cv2.threshold(
            gray,
            150,
            255,
            cv2.THRESH_BINARY
        )

        return thresh

    elif filter_name == "blur":

        return cv2.GaussianBlur(
            img,
            (5, 5),
            0
        )

    elif filter_name == "sharpen":

        kernel = [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ]

        import numpy as np

        kernel = np.array(kernel)

        return cv2.filter2D(
            img,
            -1,
            kernel
        )

    return img


def upload_image(request):

    if request.method == 'POST':

        image = request.FILES['image']

        selected_filter = request.POST.get(
            'filter',
            'none'
        )

        obj = UploadedImage.objects.create(
            image=image
        )

        start = time.time()

        img_path = obj.image.path

        img = cv2.imread(img_path)

        processed_img = apply_filter(
            img,
            selected_filter
        )

        text = pytesseract.image_to_string(
            processed_img,
            lang='spa'
        )

        end = time.time()

        obj.extracted_text = text
        obj.processing_time = end - start
        obj.text_count = len(text)

        obj.save()

        return render(
            request,
            'result.html',
            {
                'obj': obj,
                'filter': selected_filter
            }
        )

    return render(request, 'upload.html')
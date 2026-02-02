from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from datetime import date
import cv2
import numpy as np


# =========================
# HOME PAGE
# =========================
def home(request):
    return render(request, "soil_cam/index.html")


# =========================
# IMAGE ANALYSIS LOGIC
# =========================
def is_soil(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    texture = cv2.Laplacian(gray, cv2.CV_64F).var()
    return texture > 40


def extract_features(image):
    resized = cv2.resize(image, (224, 224))
    mean_color = np.mean(resized, axis=(0, 1))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    texture = cv2.Laplacian(gray, cv2.CV_64F).var()
    return mean_color, texture


def recommend_crop(mean_color, texture):
    r, g, b = mean_color

    if r < 100 and g < 100 and b < 100:
        return "Rice / Sugarcane"
    elif r > 150 and g > 130:
        return "Wheat"
    elif r > g and r > b:
        return "Cotton"
    elif texture < 60:
        return "Maize"
    else:
        return "Groundnut"


# =========================
# ANALYZE VIEW
# =========================
@csrf_exempt
def analyze(request):

    # LOAD ANALYZE PAGE
    if request.method == "GET":
        return render(request, "soil_cam/analyze.html")

    # PROCESS IMAGE
    if request.method == "POST":

        image = request.FILES.get("image")
        if not image:
            return JsonResponse({"error": "Image not received"}, status=400)

        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        path = fs.path(filename)

        img = cv2.imread(path)
        if img is None:
            return JsonResponse({"error": "Image read failed"}, status=400)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        texture = cv2.Laplacian(gray, cv2.CV_64F).var()

        if texture < 40:
            return JsonResponse({"error": "Invalid Image (Not Soil)"})

        mean_color = np.mean(img, axis=(0, 1))
        r, g, b = mean_color

        if r < 100 and g < 100 and b < 100:
            soil_type = "Black Soil"
            crop = "Rice / Sugarcane"
            confidence = "90%"
        elif r > 150 and g > 130:
            soil_type = "Alluvial Soil"
            crop = "Wheat"
            confidence = "88%"
        elif r > g and r > b:
            soil_type = "Red Soil"
            crop = "Cotton"
            confidence = "85%"
        else:
            soil_type = "Sandy Soil"
            crop = "Groundnut"
            confidence = "80%"

        return JsonResponse({
            "soil_type": soil_type,
            "recommended_crop": crop,
            "confidence": confidence,
            "temperature": request.POST.get("Temperature"),
            "location": request.POST.get("Loc_Cordinates"),
            "date": date.today().strftime("%d-%m-%Y")
        })

    return JsonResponse({"error": "Method not allowed"}, status=405)

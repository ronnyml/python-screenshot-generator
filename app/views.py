from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
from selenium import webdriver

import os

DRIVER = "chromedriver"

def home(request):
    return render(request, 'home.html', {})

def get_screenshot(request):
    width = 1024
    height = 768
    save_screenshot = False

    if request.method == 'GET' and 'url' in request.GET:
        url = request.GET['url']
        if url is not None and url != '':
            driver = webdriver.Chrome(DRIVER)
            driver.get(url)
            if 'w' in request.GET:
                width = request.GET['w']
            if 'h' in request.GET:
                height = request.GET['h']
            driver.set_window_size(width, height)
            
            if 'save' in request.GET:
            	if request.GET['save'] == 'true':
                    save_screenshot = True

            if save_screenshot:
                now = str(datetime.today().timestamp())
                img_name = "".join([now, '_image.png'])
                full_img_path = os.path.join(settings.MEDIA_ROOT, img_name)
                driver.save_screenshot(full_img_path)
                driver.quit()
                screenshot = open(full_img_path, "rb").read()
                return HttpResponse(screenshot, content_type="image/png")
            else:
                screenshot = driver.get_screenshot_as_png()
                driver.quit()
                return  HttpResponse(screenshot)
    else:
        return HttpResponse("Error")

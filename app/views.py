from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
from selenium import webdriver

import base64
import os
import urllib.parse as urlparse

DRIVER = "chromedriver"

def home(request):
    return render(request, 'home.html', {})

def get_screenshot(request):
    width = 1024
    height = 768
    save = 'false'

    if request.method == 'POST' and 'url' in request.POST:
        url = request.POST.get("url", "")
        if url is not None and url != '':
            params = urlparse.parse_qs(urlparse.urlparse(url).query)
            if len(params) > 0:
                if 'w' in params: width = int(params['w'][0])
                if 'h' in params: height = int(params['h'][0])
                if 'save' in params: save = params['save'][0]
            driver = webdriver.Chrome(DRIVER)
            driver.get(url)
            driver.set_window_size(width, height)

            if save == 'true':
                now = str(datetime.today().timestamp())
                img_name = "".join([now, '_image.png'])
                full_img_path = os.path.join(settings.MEDIA_ROOT, img_name)
                driver.save_screenshot(full_img_path)
                screenshot = open(full_img_path, "rb").read()
                var_dict = {'screenshot':img_name, 'save':True}       
            else:
                screenshot = driver.get_screenshot_as_png()
                image_64_encode = base64.encodestring(screenshot)
                var_dict = {'screenshot':image_64_encode}

            driver.quit()    
            return render(request, 'home.html', var_dict)
    else:
        return HttpResponse("Error")

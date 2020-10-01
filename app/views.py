import base64
import os
import urllib.parse as urlparse

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from datetime import datetime
from selenium import webdriver

DRIVER = 'chromedriver'

def get_screenshot(request):
    """
    Argument: Take a screenshot. 
    Return: A png file based on the url.
    """
    width = 1024
    height = 768

    if request.method == 'POST' and 'url' in request.POST:
        url = request.POST.get('url', '')
        if url is not None and url != '':
            save = False
            base_url = '{0.scheme}://{0.netloc}/'.format(urlparse.urlsplit(url))
            domain = urlparse.urlsplit(url)[1].split(':')[0]
            params = urlparse.parse_qs(urlparse.urlparse(url).query)
            if len(params) > 0:
                if 'w' in params: width = int(params['w'][0])
                if 'h' in params: height = int(params['h'][0])
            driver = webdriver.Chrome(DRIVER)
            driver.get(url)
            driver.set_window_size(width, height)

            if 'save' in params and params['save'][0] == 'true':
                save = True
                now = str(datetime.today().timestamp())
                img_dir = settings.MEDIA_ROOT
                img_name = ''.join([now, '_image.png'])
                full_img_path = os.path.join(img_dir, img_name)
                if not os.path.exists(img_dir):
                    os.makedirs(img_dir)
                driver.save_screenshot(full_img_path)
                screenshot = img_name
            else:
                screenshot_img = driver.get_screenshot_as_png()
                screenshot = base64.encodestring(screenshot_img)

            var_dict = {
                'screenshot': screenshot,
                'domain': domain,
                'base_url': base_url,
                'full_url': url,
                'save': save
            }

            driver.quit()    
            return render(request, 'home.html', var_dict)
    else:
        return render(request, 'home.html')

from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver

DRIVER = "chromedriver"

def home(request):
    return render(request, 'home.html', {})

def get_screenshot(request):
    width = 1024
    height = 768

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
            image_data = driver.get_screenshot_as_png()
            driver.quit()
            return  HttpResponse(image_data)
    else:
        return HttpResponse("Error")

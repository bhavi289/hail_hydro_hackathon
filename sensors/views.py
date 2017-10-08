from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from users.models import Users
from django.views import generic
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import time

userid = -1
plant_id = -1


@method_decorator(csrf_exempt, name='dispatch')
class sensor_data(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('this is a get request')

    def post(self, request, *args, **kwargs):
        humidity = request.POST.get("humidity", "")
        temp = request.POST.get("temp", "")
        distance = request.POST.get("distance", "")
        soilmoist = request.POST.get("soilmoist", "")
        if int(soilmoist) < 0:
            soilmoist = str(0)
        pressure = request.POST.get("pressure", "")
        altitude = request.POST.get("altitude", "")
        seapressure = request.POST.get("seapressure", "")
        user_id = request.POST.get("user_id", "")
        plant_name = request.POST.get("plant_name", "")
        p = Users.objects.filter(id=user_id)[0]
        plant_id = p.currentplant
        w = weathersensors(temp = temp, humidity = humidity, pressure = pressure, altitude = altitude, seapressure = seapressure, userid = user_id, plant_id = plant_id, time = time.strftime("%X"), date = time.strftime("%Y-%m-%d"))
        w.save()
        entryid = w.id
        s = weathersensors.objects.filter(pk=w.id)[0]
        p = plantsensors(entryid = s, soilmoisture = soilmoist)
        p.save()
        r = reservoir(entryid = s, distance = distance)
        r.save()
        return HttpResponse('DONE')

def show_list(request):
    if 'name' in request.session:
        global userid
        userid = request.session['id']
        print(userid)
        return render(request, 'sensors/temperature.html')
    else:
        return redirect('../../users/login')

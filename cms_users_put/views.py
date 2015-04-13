from django.shortcuts import render
from models import Page
from django.conf.urls import patterns, include, url
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def contentapp(request,resourceName):
	response = "<h1> WELLCOME TO THE JUNGLE! </h1>"
	if request.user.is_authenticated():
		logged = "<br><br>Logged in as " + request.user.username +\
			". <a href='/admin/logout/'>Logout</a><br>"
		if request.method == "GET":
			try:
				info = Page.objects.get(name=resourceName)
				return HttpResponse(response + info.contenido)
			except Page.DoesNotExist:
				response += '<body> Valor no encontrado, definalo </body>'
				form = "<form action='' method='POST'>\n"
				form += "Nombre: <input type='text' name='name' value='" + resourceName + "'><br>\n"
				form += "Contenido: <input type='text' name='contenido'><br>\n"
				form += "<input type='submit' value='enviar'>\n"
				form += "</form>\n"
				response += form
				response += "<a href='./admin'>Ver Base de datos</a>"
				return HttpResponse(response)
		elif request.method == "POST":
			response += '<body> POST </body>' 
			newPage = Page(name=request.POST['name'], contenido=request.POST['contenido'])
			newPage.save()
			response += "Nombre: " + request.POST['name'] 
			response += ", Contenido: " + request.POST['contenido']
			return HttpResponse(response)
		else:
			response += '<body> No way </body>'
			return HttpResponse(response)
	else:
		logged = "<br><br>Not logged. <a href='/admin/login/'>Login</a><br>"
	return HttpResponse(response + logged)

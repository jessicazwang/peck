from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from website.models import Brother
import requests
import json


def index(request):
	context = RequestContext(request)
	context_dict = {'index':True}
	return render_to_response('website/index.html',context_dict,context)

def about(request):
	context = RequestContext(request)
	context_dict = {'bold':'hi'}
	return render_to_response('website/about/about.html',context_dict,context)

def rush(request):
	context=RequestContext(request)
	return render_to_response('website/rush/rush.html',context)

def brothers(request):
	context=RequestContext(request)
	return render_to_response('website/brothers.html',context)

def house(request):
	context=RequestContext(request)
	return render_to_response('website/house.html',context)

def activities(request):
	context=RequestContext(request)
	return render_to_response('website/activities.html',context)

def national(request):
	context=RequestContext(request)
	return render_to_response('website/about/national.html',context)

def ideals(request):
	context=RequestContext(request)
	return render_to_response('website/about/ideals.html',context)

def motto(request):
	context=RequestContext(request)
	return render_to_response('website/about/motto.html',context)

def survival(request):
	context=RequestContext(request)
	return render_to_response('website/rush/survival.html',context)

def faq(request):
	context=RequestContext(request)
	return render_to_response('website/rush/faq.html',context)

def pledging(request):
	context=RequestContext(request)
	return render_to_response('website/rush/pledging.html',context)

def fifteens(request):
	context=RequestContext(request)
	fifteens_info=[]

	brothers = Brother.objects.all().order_by('name')
	for brother in brothers:
		if brother.year == 2015:
			fifteens_info.append((brother.name,brother.photo,brother.nickname,brother.initials))


	context_dict = {'fifteens_info':fifteens_info}

	return render_to_response('website/brothers/fifteens.html',context_dict,context)

def getBrother(request):
	context=RequestContext(request)
	brother_name = None

	if request.method == 'GET':
		brother_name = request.GET['bro']

	b = Brother.objects.get(initials=brother_name)
	bro = {'name':b.name,'initials':b.initials,'nickname':b.nickname,'quote':b.quote,'hometown':b.hometown,'major':b.major,'activities':b.activities,'blurb':b.blurb,'photo':b.photo}

	return HttpResponse(json.dumps(bro))

def sixteens(request):
	context=RequestContext(request)
	sixteens_info=[]

	brothers = Brother.objects.all().order_by('name')
	for brother in brothers:
		if brother.year == 2016:
			sixteens_info.append((brother.name,brother.photo,brother.nickname,brother.initials))

	context_dict = {'sixteens_info':sixteens_info}
	return render_to_response('website/brothers/sixteens.html',context_dict,context)

def seventeens(request):
	context=RequestContext(request)
	seventeens_info=[]

	brothers = Brother.objects.all().order_by('name')
	for brother in brothers:
		if brother.year == 2017:
			seventeens_info.append((brother.name,brother.photo,brother.nickname,brother.initials))

	context_dict = {'seventeens_info':seventeens_info}
	return render_to_response('website/brothers/seventeens.html',context_dict,context)

def academics(request):
	context=RequestContext(request)
	return render_to_response('website/activities/academics.html',context)

def social(request):
	context=RequestContext(request)
	return render_to_response('website/activities/social.html',context)

def community(request):
	context=RequestContext(request)
	return render_to_response('website/activities/community.html',context)

def brotherhood(request):
	context=RequestContext(request)
	return render_to_response('website/activities/brotherhood.html',context)

def athletics(request):
	context=RequestContext(request)
	return render_to_response('website/activities/athletics.html',context)

def houseprojects(request):
	context=RequestContext(request)
	return render_to_response('website/activities/houseprojects.html',context)


def first(request):
	context=RequestContext(request)
	return render_to_response('website/house/first.html',context)

def second(request):
	context=RequestContext(request)
	return render_to_response('website/house/second.html',context)

def third(request):
	context=RequestContext(request)
	return render_to_response('website/house/third.html',context)

def fourth(request):
	context=RequestContext(request)
	return render_to_response('website/house/fourth.html',context)

def roofdeck(request):
	context=RequestContext(request)
	return render_to_response('website/house/roofdeck.html',context)

def basement(request):
	context=RequestContext(request)
	return render_to_response('website/house/basement.html',context)







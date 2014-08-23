from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^rush/$',views.rush,name='rush'),
        url(r'^brothers/$',views.brothers,name='brothers'),
        url(r'^house/$',views.house,name='house'),
        url(r'^activities/$',views.activities,name='activities'),
        url(r'^national/$',views.national,name='national'),
        url(r'^ideals/$',views.ideals,name='ideals'),
        url(r'^motto/$',views.motto,name='motto'),
        url(r'^survival/$',views.survival,name='survival'),
        url(r'^faq/$',views.faq,name='faq'),
        url(r'^pledging/$',views.pledging,name='pledging'),
        url(r'^fifteens/$',views.fifteens,name='fifteens'),
        url(r'^sixteens/$',views.sixteens,name='sixteens'),
        url(r'^seventeens/$',views.seventeens,name='seventeens'),
        url(r'^academics/$',views.academics,name='academics'),
        url(r'^social/$',views.social,name='social'),
        url(r'^community/$',views.community,name='community'),
        url(r'^brotherhood/$',views.brotherhood,name='brotherhood'),
        url(r'^athletics/$',views.athletics,name='athletics'),
        url(r'^houseprojects/$',views.houseprojects,name='houseprojects'),
        url(r'^first/$',views.first,name='first'),
        url(r'^second/$',views.second,name='second'),
        url(r'^third/$',views.third,name='third'),
        url(r'^fourth/$',views.fourth,name='fourth'),
        url(r'^roofdeck/$',views.roofdeck,name='roofdeck'),
        url(r'^basement/$',views.basement,name='basement'),
        url(r'^getBrother/$',views.getBrother,name='getBrother')

        )
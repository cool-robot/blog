#-*-coding:utf-8-*-

from django.http import HttpResponse

from urllib import quote_plus



def test(request):
	return HttpResponse(quote_plus(u'这是中文'.encode('utf-8')))

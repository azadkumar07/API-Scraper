from django.shortcuts import render
import bs4
from bs4 import BeautifulSoup
from django.http import HttpResponse
import requests
from .models import API
def index(request):
	url='https://github.com/public-apis/public-apis'
	source=requests.get(url).text
	data=BeautifulSoup(source,'lxml')
	article = data.find('article')
	#title
	Title=article.p.text
	#category
	for category in article.find_all('h3'):
		print(category.text)

	for api in article.find_all('table'):
		for tr in api.tbody.find_all('tr'):
			f=0
			a=["","","","","",""]
			ind=0
			for td in tr.find_all('td'):
				ind=ind+1
				if f==0:
					f=1
					x=str(td.a)
					x=x.split("\"")
					if len(x)< 2:
						continue
					#print(x[1])
					a[0]=x[1]
				a[ind]=td.text
				#print(td.text,' ')
			#print('')
			data=API(API_Name=a[1],API_Link=a[0],API_Des=a[2],API_Auth=a[3],API_HTTPS=a[4],API_CORS=a[5])
			data.save()

	return HttpResponse('HELLO')


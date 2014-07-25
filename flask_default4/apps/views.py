from flask import Flask, render_template, request, redirect
from apps import app
import webbrowser
from bs4 import BeautifulSoup
import urllib2

from flaskext import wtf
from flaskext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

@app.route('/', methods=['GET', 'POST'])
def get():
    return render_template("index.html")

@app.route('/crawl', methods=['GET', 'POST'])
def crawl():
	result=[]

	if request.method == 'GET':
		basicurl = "http://news.naver.com/main/search/search.nhn?query="
		# url = basicurl + URLEncoder.encode(request.args['search'], "UTF-8")
		# urllib.urlretrieve(urllib.quote(url.encode('utf8'), '/:'))

		url = basicurl + request.args['search']
		# url = url.encode('utf-8')
		# url = urllib2.quote(url.encode('utf-8'), '/:')
		# url = urllib.quote(url.encode('utf-8'), '/:')


		# return url
		return redirect(url)

	if request.method == 'POST':
		url_pre = "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1="
		try:
			if request.form['politics']:

				url = url_pre+str(request.form['politics'])
				htmltext = urllib2.urlopen(url).read().decode('euc-kr', 'ignore')
				soup = BeautifulSoup(htmltext, from_encoding="euc-kr")

				# for each in soup.findAll('h5', attrs={'class': 'compo_headtxt'}):
				# 	result.append( each.string )

				for each in soup.findAll('dt'):
					try:
						# result.append(each.a.string)

						if not each.a.string==None:
							result.append(each.a.string)
					except:
						pass

				return render_template("index.html", result =result)
		except Exception, e:
			pass

		try:
			if request.form['economy']:
				url = url_pre+str(request.form['economy'])
				htmltext = urllib2.urlopen(url).read().decode('euc-kr', 'ignore')
				soup = BeautifulSoup(htmltext, from_encoding="euc-kr")

				# for each in soup.findAll('h5', attrs={'class': 'compo_headtxt'}):
				# 	result.append( each.string )
				for each in soup.findAll('dt'):
					try:
						if not each.a.string==None:
							result.append(each.a.string)
					except:
						pass		
				return render_template("index.html", result =result)
		except Exception, e:
			pass

		try:
			if request.form['social']:
				url = url_pre+str(request.form['social'])
				htmltext = urllib2.urlopen(url).read().decode('euc-kr', 'ignore')
				soup = BeautifulSoup(htmltext, from_encoding="euc-kr")

				# for each in soup.findAll('h5', attrs={'class': 'compo_headtxt'}):
				# 	result.append( each.string )
				for each in soup.findAll('dt'):
					try:
						if not each.a.string==None:
							result.append(each.a.string)
					except:
						pass		
						
				return render_template("index.html", result =result)
		except Exception, e:
			pass

		try:
			if request.form['life']:
				url = url_pre+str(request.form['life'])
				htmltext = urllib2.urlopen(url).read().decode('euc-kr', 'ignore')
				soup = BeautifulSoup(htmltext, from_encoding="euc-kr")

				# for each in soup.findAll('h5', attrs={'class': 'compo_headtxt'}):
				# 	result.append( each.string )
				for each in soup.findAll('dt'):
					try:
						if not each.a.string==None:
							result.append(each.a.string)
					except:
						pass
				return render_template("index.html", result =result)
		except Exception, e:
			pass

		try:
			if request.form['world']:
				url = url_pre+str(request.form['world'])
				htmltext = urllib2.urlopen(url).read().decode('euc-kr', 'ignore')
				soup = BeautifulSoup(htmltext, from_encoding="euc-kr")

				# for each in soup.findAll('h5', attrs={'class': 'compo_headtxt'}):
				# 	result.append( each.string )
				for each in soup.findAll('dt'):
					try:
						if not each.a.string==None:
							result.append(each.a.string)
					except:
						pass
				return render_template("index.html", result =result)
		except Exception, e:
			pass

		try:
			if request.form['IT']:
				url = url_pre+str(request.form['IT'])
				htmltext = urllib2.urlopen(url).read().decode('euc-kr', 'ignore')
				soup = BeautifulSoup(htmltext, from_encoding="euc-kr")

				# for each in soup.findAll('h5', attrs={'class': 'compo_headtxt'}):
				# 	result.append( each.string )
				for each in soup.findAll('dt'):
					try:
						if not each.a.string==None:
							result.append(each.a.string)
					except:
						pass
				return render_template("index.html", result =result)
		except Exception, e:
			pass

		try:
			if request.form['entertain']:
				url = url_pre+str(request.form['entertain'])
				htmltext = urllib2.urlopen(url).read().decode('euc-kr', 'ignore')
				soup = BeautifulSoup(htmltext, from_encoding="euc-kr")

				# for each in soup.findAll('h5', attrs={'class': 'compo_headtxt'}):
				# 	result.append( each.string )
				for each in soup.findAll('dt'):
					try:
						if not each.a.string==None:
							result.append(each.a.string)
					except:
						pass	
				return render_template("index.html", result =result)
		except Exception, e:
			pass




	return render_template("index.html")










from zomato_st import *
from threading import *

# class ClassName(object):
	# """docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
		# self.arg = arg
		
def page_all(n,page_no):
	final_list=[]
	if os.path.exists('zomato('+str(n)+'page '+str(page_no)+").json")==False:
	
		final_dic_1={}
		URL_1 = st_[n]+'?page='+str(page_no)     
		driver_1 = webdriver.Chrome(ChromeDriverManager().install())
		driver_1.get(URL_1)
		page_1=driver_1.execute_script("return document.documentElement.outerHTML")
		driver_1.quit()
		soup_1=BeautifulSoup(page_1,"html.parser")
		div=soup_1.find('div',id='orig-search-list',class_='ui cards')
		div_all=div.find_all('div',class_="card search-snippet-card search-card")
		
		for i in div_all:
			l=i.find('a',class_="result-title hover_feedback zred bold ln24 fontsize0" )
			if l!=None:
				final_dic_1['Name']=l.text.strip()
			l=i.find('div' ,class_="ta-right floating search_result_rating col-s-4 clearfix")
			if l!=None:	
				final_dic_1['Rating']=(l.text.split())[0]
			l=l.find('span')
			if l!=None:
				final_dic_1['votes']=(l.text.split())[0]
			l=i.find('div',class_="col-m-16 search-result-address grey-text nowrap ln22")
			if l!=None:
				final_dic_1['location']=l.text
			div=i.find('span',class_="col-s-11 col-m-12 nowrap pl0")
			if div!=None:
				div=(div.text)
				span=i.find('span', class_="col-s-5 col-m-4 ttupper fontsize5 grey-text").text
				final_dic_1[span]=div
			time_=(i.find('div',class_="res-timing clearfix"))
			if time_!=None:
				time_=time_.text.split()
				l=''
				for k in range(1,len(time_)):
					l+=time_[k]
				final_dic_1[time_[0][:-1].lower()]=l
			div=i.find('div',class_='res-cost clearfix')
			if div!=None:
				div=(div.text).split(':')
				final_dic_1[div[0]]=div[1]
			
			div=i.find('div',class_='res-collections clearfix')
			if div!=None:
				span=div.find('span',class_='col-s-5 col-m-4 ttupper fontsize5 grey-text')
		
				stt=div.find('div',class_="col-s-11 col-m-12 pl0 search-grid-right-text")
				final_dic_1[span.text]=stt.text
			div=i.find('div',class_='col-s-11 col-m-12 pl0 search-grid-right-text')
			if div!=None:
				a=div.find('a')
				if a!=None:
					final_dic_1['discount']=a.text.strip()
			
			final=copy.deepcopy(final_dic_1)
			final_list.append((final))
		
		pprint.pprint(final_list)
		a=open('zomato('+str(n)+'page '+str(page_no)+").json",'w')
		json.dump(final_list,a)
		a.close()
		time.sleep(1)
	# page_no+=1






def location(n,last_page):
	
	# return last_page
	page_no=695
	while page_no<=last_page:
		print(page_no)

		class s1(Thread):
			def run(self):
				page_all(n,page_no)


		class s2(Thread):
			def run (self):
				page_all(n,page_no+1)

		class s3(Thread):
			def run (self):
				page_all(n,page_no+2)

		class s4(Thread):
			def run (self):
				page_all(n,page_no+3)

		class s5(Thread):
			def run (self):
				page_all(n,page_no+4)
		t1=s1()
		t2=s2()
		t3=s3()
		t4=s4()
		t5=s5()

		t1.start()
		time.sleep(3)
		t2.start()
		time.sleep(3)
		t3.start()
		time.sleep(3)
		t4.start()
		time.sleep(3)

		page_no+=5
		# t1.join()
		# time.sleep(1)
		# t2.join()
		# time.sleep(1)
		# t3.join()
		# time.sleep(1)
		# t4.join()
		# time.sleep(1)
		# t5.join()

		
		# final_list=[]
		# if os.path.exists('zomato('+str(n)+'page '+str(page_no)+").json")==False:
		
		# 	final_dic_1={}
		# 	URL_1 = st_[n]+'?page='+str(page_no)     
		# 	driver_1 = webdriver.Chrome(ChromeDriverManager().install())
		# 	driver_1.get(URL_1)
		# 	page_1=driver_1.execute_script("return document.documentElement.outerHTML")
		# 	driver_1.quit()
		# 	soup_1=BeautifulSoup(page_1,"html.parser")
		# 	div=soup_1.find('div',id='orig-search-list',class_='ui cards')
		# 	div_all=div.find_all('div',class_="card search-snippet-card search-card")
			
		# 	for i in div_all:
		# 		l=i.find('a',class_="result-title hover_feedback zred bold ln24 fontsize0" )
		# 		if l!=None:
		# 			final_dic_1['Name']=l.text.strip()
		# 		l=i.find('div' ,class_="ta-right floating search_result_rating col-s-4 clearfix")
		# 		if l!=None:	
		# 			final_dic_1['Rating']=(l.text.split())[0]
		# 		l=l.find('span')
		# 		if l!=None:
		# 			final_dic_1['votes']=(l.text.split())[0]
		# 		l=i.find('div',class_="col-m-16 search-result-address grey-text nowrap ln22")
		# 		if l!=None:
		# 			final_dic_1['location']=l.text
		# 		div=i.find('span',class_="col-s-11 col-m-12 nowrap pl0")
		# 		if div!=None:
		# 			div=(div.text)
		# 			span=i.find('span', class_="col-s-5 col-m-4 ttupper fontsize5 grey-text").text
		# 			final_dic_1[span]=div
		# 		time_=(i.find('div',class_="res-timing clearfix"))
		# 		if time_!=None:
		# 			time_=time_.text.split()
		# 			l=''
		# 			for k in range(1,len(time_)):
		# 				l+=time_[k]
		# 			final_dic_1[time_[0][:-1].lower()]=l
		# 		div=i.find('div',class_='res-cost clearfix')
		# 		if div!=None:
		# 			div=(div.text).split(':')
		# 			final_dic_1[div[0]]=div[1]
				
		# 		div=i.find('div',class_='res-collections clearfix')
		# 		if div!=None:
		# 			span=div.find('span',class_='col-s-5 col-m-4 ttupper fontsize5 grey-text')
			
		# 			stt=div.find('div',class_="col-s-11 col-m-12 pl0 search-grid-right-text")
		# 			final_dic_1[span.text]=stt.text
		# 		div=i.find('div',class_='col-s-11 col-m-12 pl0 search-grid-right-text')
		# 		if div!=None:
		# 			a=div.find('a')
		# 			if a!=None:
		# 				final_dic_1['discount']=a.text.strip()
				
		# 		final=copy.deepcopy(final_dic_1)
		# 		final_list.append((final))
			
		# 	pprint.pprint(final_list)
		# 	a=open('zomato('+str(n)+'page '+str(page_no)+").json",'w')
		# 	json.dump(final_list,a)
		# 	a.close()
		# 	time.sleep(1)
		# page_no+=1
		
	all_list=[]
	for i in range(1,last_page+1):
		a=open('zomato('+str(n)+'page '+str(i)+").json",'r')
		file=json.load(a)
		a.close()
		all_list.append(file)

# 

st_=data()
for i in st_:
	URL = st_[i]   
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get(URL)
	page=driver.execute_script("return document.documentElement.outerHTML")
	driver.quit()
	soup=BeautifulSoup(page,"html.parser")
	div=soup.find('div',class_="search-pagination-top clearfix mtop")
	div=div.find('div',class_="col-l-4 mtop pagination-number")
	div=div.text.split()
	print(div[-1])
	pprint.pprint(location(i,int(div[-1])))
	time.sleep(1)
	break

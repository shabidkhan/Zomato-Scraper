from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from bs4 import BeautifulSoup               
import time,pprint,json,os,copy
 
def data():
	if os.path.exists("zomato_st.json")==False:
		final_dic={}
		URL = 'https://www.zomato.com/ncr'     
		driver = webdriver.Chrome(ChromeDriverManager().install())
		driver.get(URL)
		page=driver.execute_script("return document.documentElement.outerHTML")
		driver.quit()

		soup=BeautifulSoup(page,"html.parser")
		div=soup.find('div',class_="ui segment row")
		a=div.find_all('a')
		st_dic={}
		for i in a:
			i_list=(i.text.split())
			l=''
			for k in range(len(i_list)):
				if k==len(i_list)-1:
					l+=i_list[k]
				else:
					l+=i_list[k]+' '
			st_dic[l]=str(i['href'])
		a=open('zomato_st.json','w')
		json.dump(st_dic,a)
		a.close()

	a=open('zomato_st.json','r')
	st_=json.load(a)
	a.close()
	return(st_)

if __name__=="__main__":
	pprint.pprint(data())

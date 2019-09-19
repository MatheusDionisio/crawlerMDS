#import requests
import bs4
import urllib2
url=raw_input('insira o site : ')
#code with requests lib{
#resposta=bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
#urlib2 pode ser usada para o mesmo proposito que a lib requests sendo o request.get()==urllib2.urlopen().read()} 
resposta=bs4.BeautifulSoup(urllib2.urlopen(url).read(),'html.parser')
arquivo=open('arquivo.txt','w')
link=open('link.txt','w')
#code with requests lib{
#resposta_text=resposta.text
#resposta_soup= bs4.BeautifulSoup(resposta_text)}
for token in resposta.findAll('a'):
	arquivo.write(token.get_text().encode('utf-8'))
	link.write(str(token.get('href'))+'\n')
arquivo.close()
link.close
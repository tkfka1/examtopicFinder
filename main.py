from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import json

link_dic = {}

## 문제갯수
for i in range(1,551):
    link_dic[i] = []

## 페이지 갯수
for i in range(1,533):

    html = Request("https://www.examtopics.com/discussions/amazon/"+str(i)+"/",headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})  
    webpage = urlopen(html).read()

    bsObject = BeautifulSoup(webpage, "html.parser") 

    # print(bsObject) # 웹 문서 전체가 출력됩니다. 

    # print(bsObject.head.title)

    # for meta in bsObject.head.find_all('meta'):
    #     print(meta.get('content'))

    # print (bsObject.head.find("meta", {"name":"description"}))

    # print (bsObject.head.find("meta", {"name":"description"}).get('content'))

    for link in bsObject.find_all('a'):
        temp1 = link.text.strip()
        temp2 = link.get('href')
        temp3 = temp1.split()
        if "Exam AWS Certified Solutions Architect - Associate SAA-C03" in temp1:
            link_dic[int(temp3[11])].append("https://www.examtopics.com"+temp2)

    print(f"end {i}")
# print(link_dic)

with open('link.json', 'w') as f : 
	json.dump(link_dic, f, indent=4)
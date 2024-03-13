import requests
import pprint
import json

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttblurelight1516001'
params = {
    'ttbkey': API_KEY,
    'QueryType' : 'ItemNewSpecial',
    'Start' : 1,
    'MaxResults' : 50,
    'SearchTarget' : 'Book',
    'Output' : 'JS',
    'Version' : 20131101
}

response = requests.get(API_URL, params=params)
contents = response.text
js_contents = json.loads(contents)
pp = pprint.PrettyPrinter(indent=7)
# print(pp.pprint(js_contents))
# print(type(js_contents))

# print({'제목 :',  js_contents['title'], '저자 : ', js_contents['author']})
# print(len(js_contents))
# print(js_contents['item'])
books=[]
for i in js_contents['item']:
    info={
        '국제 표준 도서 번호' : i['isbn'],
        '저 자' : i['author'],
        '제 목' : i['title'],
        '출간일': i['pubDate']
    }
    books.append(info)
    print(pp.pprint(books))



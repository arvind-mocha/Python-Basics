import requests
import concurrent.futures
import os

os.chdir('E:\PYTHON_BASICS_SAVES\multiprocessing_package')
url = ['https://images.unsplash.com/photo-1588802566325-e612541ac61b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
       'https://images.unsplash.com/photo-1587668880216-4af3a9267cb6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
       'https://images.unsplash.com/photo-1548016732-cdee825735fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'
       ]

s_url1 = []
for i in url:
    s_url2 = i.split('?',1)[0]#1 discribes split all after ?
    s_url1.append(s_url2)

for i in s_url1:
    name = i.split('/')[3]
    name = f'{name}.jpg'
    bytes = requests.get(i).content
    with open(name,'wb') as f:
        f.write(bytes)
        print('img printed',i)

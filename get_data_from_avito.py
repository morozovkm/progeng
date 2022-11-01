import requests

html = requests.get('https://www.maxidom.ru/search/catalog/?q=%D0%BA%D1%80%D0%B0%D1%81%D0%BA%D0%B0').text
print(html)

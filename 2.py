import requests

response1 = requests.get('https://catalog.api.2gis.com/3.0/items/geocode?q=Екатеринбург, ул. Вайнера, д. 16&fields=items.point&key=YOUR_KEY') #Получаем координаты
#Для получения координат нужен API KEY, для усорения процесса в рамках задачи внесем координаты вручную

zdanie1=[56.835018, 60.594977] #Екатеринбург, ул. Вайнера, д. 16 здесь вставить результат запроса
zdanie2=[56.840646, 60.612180] #Екатеринбург, ул. Карла Либкнехта, д. 22
h1=3*3 #3 этажа
h2=7*3 #7 этажей

d=abs(zdanie2[0]-zdanie1[0])+abs(zdanie2[1]-zdanie1[1])*100*1000
print(d,'метров')

l=h1*2+h2*2+d

print('Длина кабеля между зданием 1 и 2=',l,'метров')
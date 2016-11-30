import vk
import time
print('vk photos geo location')
#id=5742347
#API=AIzaSyAD9cDsgLaCwRQrIZgdPTMd_xG3tfMjhDg

session = vk.Session('dc9cb414fc28a2d1cbb4d761ab53ba04fd0adcc738314f2492b28656f09fcae2eee035c4e4de85ad84e34')
#session = vk.AuthSession('app  id', 'user login', 'user password')

api = vk.API(session)
friends=api.friends.get()

print(len(friends))
print(friends)

friends = api.friends.get()

friends_info = api.users.get(user_ids=friends)

for friend in friends_info:
    print('ID %s Имя: %s %s' % (friend['uid'], friend['last_name'], friend['first_name']))
geolocation = []

for id in friends:
    print('Получаем данные пользователя: %s' % id)
    albums = api.photos.getAlbums(owner_id=id)
    print('\t...альбомов %s...' % len(albums))
    for album in albums:
        try:
            photos = api.photos.get(owner_id=id, album_id=album['aid'])
            print('\t\t...обрабатываем фотографии альбома...')
            for photo in photos:
                if 'lat' in photo and 'long' in photo:
                    geolocation.append((photo['lat'], photo['long']))
            print('\t\t...найдено %s фото...' % len(photos))
        except:
            pass
        time.sleep(0.5)
    time.sleep(0.5)
js_code = ""
for loc in geolocation:
    js_code += 'new google.maps.Marker({ position: {lat: %s, lng: %s}, map: map });\n' % (loc[0], loc[1])
html=open('map.html').read()
html = html.replace('/* PLACEHOLDER */', js_code)
f = open('vkphotosgeolocation.html','w')
f.write(html)
f.close()


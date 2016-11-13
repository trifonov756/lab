import pyowm
import datetime
print("OpenwWeatherMap")
owm = pyowm.OWM('e62ffe0bbe512eedc24c893c6f199bd7')
observation = owm.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()
print(owm)
print(observation)
print(weather)
print(location)

print('Страна: ' + location.get_country())
print('Город: ' + location.get_name())
print('Долгота: ' + str(location.get_lon()))
print('Широта: ' + str(location.get_lat()))
print('Облачность: ' + str(weather.get_clouds()))
print('Статус: ' + str(weather.get_detailed_status()))
print('Давление: ' + str(weather.get_pressure()))
print('Дождь: ' + str(weather.get_rain()))
print('Снег: ' + str(weather.get_snow()))
print('Время: ' + str(weather.get_reference_time('iso')))
print('Статус: ' + str(weather.get_status()))
print('Восход: ' + str(weather.get_sunrise_time('iso')))
print('Закат: ' + str(weather.get_sunset_time('iso')))
print('Температура: ' + str(weather.get_temperature('celsius')))
print('Видимость: ' + str(weather.get_visibility_distance()))
print('Изображение: ' + weather.get_weather_icon_name())
print('Ветер: ' + str(weather.get_wind()))

now = datetime.datetime.now()
observation = owm.weather_at_place('Moscow,ru')
location = observation.get_location()
def Cloud():
    if 0 <= weather.get_clouds() <= 20:
        return 'ясная'
    if 20<=weather.get_clouds()<=40:
        return 'облачная'
    if 40<=weather.get_clouds()<=20:
        return 'пасмурная'
translate = {'Moscow':'Москва ','RU':'Россия'}
print('Погода в городе ' + translate[location.get_name()] +'(' + translate[location.get_country()] + ') на сегодня в ' + now.strftime("%H:%M") + ' облачность составляет '+ str(weather.get_clouds())+ '% давление составляет ' + str(weather.get_pressure())+ 'температура' + str(weather.get_temperature('celsius')) +' градусов цельсия, '+ 'ветер' + str(weather.get_wind()))

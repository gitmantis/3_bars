# Ближайшие бары

[Скрипт bars.py находит информацию о барах с минимальным и максимальным количеством мест, а также бар, расстояние до которого минимально относительно введенных пользователем координат]

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python
Enter json filepath:data-2897-2016-11-23.json
Enter your latitude:35
Enter your longitude:56

Biggest bar: 

{'Address': ' ,  23,  1',
 'AdmArea': '  ',
 'District': ' ',
 'ID': '00138530',
 'IsNetObject': '',
 'Latitude_WGS84': '55.7011146292467670',
 'Longitude_WGS84': '37.6382285008039050',
 'Name': '   ',
 'PublicPhone': [{'PublicPhone': '(905) 795-15-84',
                  'global_id': 33761.0,
                  'global_object_id': 169375059.0,
                  'system_object_id': '00138530 _1'}],
 'SeatsCount': 450,
 'SocialPrivileges': '',
 'TypeObject': '',
 'geoData': {'coordinates': [37.638228501070095, 55.70111462948684],
             'type': 'Point'},
 'global_id': 169375059,
 'system_object_id': '00138530'}

Smallest bar: 

{'Address': ' ,  34/29',
 'AdmArea': '-  ',
 'District': ' ',
 'ID': '00107283',
 'IsNetObject': '',
 'Latitude_WGS84': '55.8461447588834330',
 'Longitude_WGS84': '37.3580592058223000',
 'Name': '. ',
 'PublicPhone': [{'PublicPhone': '(495) 258-94-19',
                  'global_id': 22348.0,
                  'global_object_id': 20675518.0,
                  'system_object_id': '00107283 _1'}],
 'SeatsCount': 0,
 'SocialPrivileges': '',
 'TypeObject': '',
 'geoData': {'coordinates': [37.35805920566864, 55.84614475898795],
             'type': 'Point'},
 'global_id': 20675518,
 'system_object_id': '00107283'}

Closest bar: 

{'Address': ' ,  1',
 'AdmArea': '  ',
 'District': ' ',
 'ID': '000080078',
 'IsNetObject': '',
 'Latitude_WGS84': '55.4487502800000000',
 'Longitude_WGS84': '37.5112750000000000',
 'Name': ' ',
 'PublicPhone': [{'PublicPhone': '(495) 867-55-75',
                  'global_id': 24143.0,
                  'global_object_id': 20728003.0,
                  'system_object_id': '000080078_1'}],
 'SeatsCount': 35,
 'SocialPrivileges': '',
 'TypeObject': '',
 'geoData': {'coordinates': [37.511274999942046, 55.448750279822924],
             'type': 'Point'},
 'global_id': 20728003,
 'system_object_id': '000080078'}

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

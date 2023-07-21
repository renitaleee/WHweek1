import urllib.request as request
import json
import csv
from collections import defaultdict

src = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'

with request.urlopen(src) as response:
    data = json.load(response)

attractions = data['result']['results']
attraction_data = []
mrt_data = defaultdict(list) # 捷運站名稱:[景點1, 景點2...]

for attraction in attractions:
    attraction_info = []

    # 處理與attraction.csv相關的資料
    attraction_info.append(attraction['stitle']) # 景點名稱
    attraction_info.append(attraction['address'][5:8]) # 區域
    attraction_info.append(attraction['longitude']) # 經度
    attraction_info.append(attraction['latitude']) # 緯度
    urls = attraction['file'].split('https') #圖片連結
    for url in urls:
        if '.jpg' in url or '.JPG' in url:
            attraction_info.append('https'+url)
            break
    attraction_data.append(attraction_info)

    # 處理與mrt.csv相關的資料
    if attraction['MRT'] == None:
        pass
    else:
        mrt_data[attraction['MRT']].append(attraction['stitle'])

with open('attraction.csv', 'w', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    for attraction in attraction_data:
        writer.writerow(attraction)

with open('mrt.csv', 'w', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    for mrt in mrt_data:
        info_lst = []
        info_lst.append(mrt)
        for attraction in mrt_data[mrt]:
            info_lst.append(attraction)
        writer.writerow(info_lst)
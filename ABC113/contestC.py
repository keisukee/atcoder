N, M = list(map(int, input().split()))
prefectures = [[] for i in range(N)]
cities = [None] * M

for i in range(M):
    belongsTo, year = list(map(int, input().split()))
    prefectures[belongsTo-1].append({'year': year, 'number': i})

for prefId, prefecture in enumerate(prefectures):
    prefecture.sort(key = lambda x: x['year'])
    for i, city in enumerate(prefecture):
        year = city['year']
        number = city['number']
        cityId = str(prefId+1).zfill(6) + str(i+1).zfill(6)
        cities[number] = cityId

# print('prefectures', prefectures)
for city in cities:
    print(city)


def solution(cacheSize, cities):
    cache = []
    t = 0
    cities = [i.upper() for i in cities]
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        # 캐시 미스
        if city not in cache:
            # 캐시가 가득
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
            t += 5
        # 캐시 히트
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            t += 1
    print(t)
    return t


solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
             "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3,	["Jeju", "Pangyo", "Seoul", "Jeju",
             "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
             "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
             "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(2,	["Jeju", "Pangyo", "NewYork", "newyork"])

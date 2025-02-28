'''Labs 08.03 - Set Covering'''
import json
def find_stations(stations : list, cities_list :list):
    bought_stations = []
    while cities_list:
        # print(f"{cities_list}")
        # print([station["Name"] for station in bought_stations])
        most_coverage = None
        most_coverage_num = 0
        for station in stations:
            cities = station["Cities"]
            coverage_num = 0
            for city1 in cities:
                for city2 in cities_list:
                    if city1 == city2:
                        coverage_num += 1
                        break
            if coverage_num > most_coverage_num:
                most_coverage_num = coverage_num
                most_coverage = station
        if most_coverage == None:
            break
        bought_stations.append(most_coverage)
        remove_same(cities_list, most_coverage["Cities"])
    print(sorted([station["Name"] for station in bought_stations]))

def remove_same(cities_list : list, cities : list):
    for city_target in cities:
        for i, city in enumerate(cities_list):
            if city == city_target:
                cities_list.pop(i)
                break

def main():
    cities_list = json.loads(input())
    station_num = int(input())
    stations = []
    for _ in range(station_num):
        stations.append(json.loads(input()))
    find_stations(stations, cities_list)

main()

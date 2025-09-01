# # import requests

# # url = "https://kiwi-com-cheap-flights.p.rapidapi.com/one-way"
# src_city = "boston_ma_us"
# dest_city = "orlando_fl_us"
# querystring = {"source":f"City:{src_city}","destination":f"City:{dest_city}r","currency":"usd","locale":"en","adults":"1","children":"0","infants":"0","handbags":"1","holdbags":"0","cabinClass":"ECONOMY","sortBy":"QUALITY","applyMixedClasses":"true","allowChangeInboundDestination":"true","allowChangeInboundSource":"true","allowDifferentStationConnection":"true","enableSelfTransfer":"true","allowOvernightStopover":"true","enableTrueHiddenCity":"true","allowReturnToDifferentCity":"false","allowReturnFromDifferentCity":"false","enableThrowAwayTicketing":"true","outbound":"SUNDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,MONDAY,TUESDAY","transportTypes":"FLIGHT","contentProviders":"FLIXBUS_DIRECTS,FRESH,KAYAK,KIWI","limit":"20"}

# # headers = {
# # 	"x-rapidapi-key": "397f33e22bmsh01328fc3eb3099cp1fc14ejsnca5184158bdb",
# # 	"x-rapidapi-host": "kiwi-com-cheap-flights.p.rapidapi.com"
# # }

# # response = requests.get(url, headers=headers, params=querystring)

# # print(response.json())

# tom = "yomama"
# str = {f"hello {tom}", f"hello {city}"}
# print(str)

airports = ["JFK", "LOG", "LAX"]

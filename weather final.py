
import requests

city_name = input("Enter your city: ")

Zip_Code = input("Enter you Zip code: ")

api_key1 = "b0dcab972b6b94eb98d5811544648c81"

api_key2 = "2e016624f7d56f526ea060e5a126283b2aa0620c"

api_key3 = "b0dcab972b6b94eb98d5811544648c81"

url1 = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key1}&units=metric"

url2 = f"https://api.waqi.info/feed/{city_name}/?token={api_key2}"

url3 = f"https://api.openweathermap.org/data/2.5/weather?zip={Zip_Code},in&appid={api_key3}&units=metric"

response1 = requests.get(url1)

response2 = requests.get(url2)

response3 = requests.get(url3)

data1 = response1.json()

data2 = response2.json()

data3 = response3.json()

aqi = data2['data']['aqi']

print ("Your location :",data3["name"])

print (f"The Air Quality Index in {city_name} is {aqi}")

print ("Current Temperature :",data1["main"]["temp"])

print ("Current Temperature Feels Like: ",data1["main"]["feels_like"])

print ("Maximum Temperature: ",data1["main"]["temp_max"])

print ("Minimum Temperature: ",data1["main"]["temp_min"])

print ("Current Pressure: ",data1["main"]["pressure"])

print ("current Humidity: ",data1["main"]["humidity"])

print ("Visibility: ",data1["visibility"])

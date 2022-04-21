from weatherapi.weatherapi_client import WeatherapiClient
import datetime

key = '86fb5d55391f4825963220642222004'
client = WeatherapiClient(key)
ap_is_controller = client.ap_is

q = 'Fremont'
print(q)
end_dt = datetime.datetime.now().date()
days = datetime.timedelta(6)
from_dt = end_dt - days
print('from date:', from_dt)
print('end date:', end_dt)
result = ap_is_controller.get_history_weather(q = q, dt = from_dt, end_dt = end_dt)
print(len(result.forecast.forecastday))
print(len(result.forecast.forecastday[0].hour))

for hour_obj in result.forecast.forecastday[0].hour:
    print(hour_obj.time, hour_obj.feelslike_f)

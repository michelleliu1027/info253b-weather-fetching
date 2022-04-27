from weatherapi.weatherapi_client import WeatherapiClient
import datetime
import pandas as pd

key = '86fb5d55391f4825963220642222004'
client = WeatherapiClient(key)
ap_is_controller = client.ap_is

cities = ['Berkeley', 'Oakland', 'San Francisco']
output = {'city_name':[], 'date':[], 'temperature':[]}
for city in cities:
    print(city)
    end_dt = datetime.datetime.now().date()
    days = datetime.timedelta(6)
    from_dt = end_dt - days
    print('from date:', from_dt)
    print('end date:', end_dt)
    result = ap_is_controller.get_history_weather(q = city, dt = from_dt, end_dt = end_dt)
    print(result.forecast.forecastday)
    for day in result.forecast.forecastday:
        for hour_obj in day.hour:
            output['city_name'].append(city)
            output['date'].append(hour_obj.time)
            output['temperature'].append(hour_obj.feelslike_f)
print(pd.DataFrame(output))
pd.DataFrame(output).to_csv('city_temp.csv')

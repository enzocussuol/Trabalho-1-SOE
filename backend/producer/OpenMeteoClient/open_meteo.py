import requests
from datetime import *
from OpenMeteoClient.capitals import CAPITALS,Location


class OpenMeteo():
    def __init__(self,locations = [Location(-20.32,-40.34,"Casa Bonella"), Location(-20.18,-40.25,"Casa Enzo"), Location(-20.26,-40.28,"Casa Dudu")]):
        # Locais de interesse
        # location = Class Location

        self.locations = CAPITALS
        # self.locations = locations
    
    def get_locations_weather(self):
        print("OBTENDO DADOS...")
        infos = []
        for key,value in self.locations.items():
            value.set_code(key)
            infos.append(self.__get_current_location(value))
        
        print("ACABO")
        return {'data': infos}
    
    def __get_current_location(self, location):
        data = requests.get(self.__format_url(location.get_lat(), location.get_long())).json()
        current = data["current_weather"]
        current_time = datetime.strptime(current["time"], "%Y-%m-%dT%H:%M")

        return {"location":str(location), "code": location.cod, "data":{"time":str(current_time), "temperature": current["temperature"], "precipitation": data["hourly"]["precipitation_probability"][current_time.hour], "windspeed":current["windspeed"], "uv_index_max": data["daily"]["uv_index_max"][0]}}

    def __format_url(self,latitude,longitude):
        return f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation_probability,windspeed_10m&daily=uv_index_max&forecast_days=1&timezone=America%2FSao_Paulo&current_weather=true"

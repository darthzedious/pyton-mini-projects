import requests

def get_weather():
    """ This function is set to return the current, daily(in range next 7 days) and hourly  time, temperature etc.
    in Sofia, Bulgaria.
    lattitude and longitude are representing the geographical coordinates of the city.
    :return:
    """
    url = "https://api.open-meteo.com/v1/forecast?latitude=42.6975&longitude=23.3241&" \
          "current=temperature_2m,is_day,rain,windspeed_10m,winddirection_10m&" \
          "hourly=temperature_2m,rain,windspeed_10m,winddirection_10m&" \
          "daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset&timezone=auto"
    try:
        response = requests.get(url)
        date = response.json()
        current = date["current"]
        daily = date["daily"]
        hourly = date["hourly"]
        return current, daily, hourly

    except requests.exceptions.RequestException as e:
        print("Error", e)


print(get_weather())

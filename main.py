import OpenMeteoClient as omc

def main():
    client = omc.OpenMeteo()
    print(client.get_locations_weather())

if __name__ == "__main__":
    main()

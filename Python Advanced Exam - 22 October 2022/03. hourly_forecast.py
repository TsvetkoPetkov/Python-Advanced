def forecast(*args):
    sunny_dict = {}
    cloudy_dict = {}
    rainy_dict = {}

    for forecast_info in args:
        city_name, weather = forecast_info

        if weather == "Sunny":
            if city_name not in sunny_dict:
                sunny_dict[city_name] = ""

            sunny_dict[city_name] += weather
        elif weather == "Cloudy":
            if city_name not in cloudy_dict:
                cloudy_dict[city_name] = ""

            cloudy_dict[city_name] += weather
        elif weather == "Rainy":
            if city_name not in rainy_dict:
                rainy_dict[city_name] = ""

            rainy_dict[city_name] += weather

    sorted_sunny = dict(sorted(sunny_dict.items(), key=lambda kvp: kvp[0]))
    sorted_cloudy = dict(sorted(cloudy_dict.items(), key=lambda kvp: kvp[0]))
    sorted_rainy = dict(sorted(rainy_dict.items(), key=lambda kvp: kvp[0]))

    output = ""

    if sorted_sunny:
        for c, w in sorted_sunny.items():
            output += f"{c} - {w}\n"

    if sorted_cloudy:
        for c, w in sorted_cloudy.items():
            output += f"{c} - {w}\n"

    if sorted_rainy:
        for c, w in sorted_rainy.items():
            output += f"{c} - {w}\n"

    return output.strip()

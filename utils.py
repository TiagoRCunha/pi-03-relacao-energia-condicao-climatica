from geopy.geocoders import Nominatim


def get_cities_names(df):
    """
    Recebe um DataFrame com os campos "latitude" e "longitude",
    esses campos são utilizados para pegar o nome da cidade com o geopy.
    Os valores devem ser do tipo float.

    Retorna uma lista com os nomes das cidades.
    """
    geolocator = Nominatim(
        user_agent="projeto_integrador_app", domain="localhost:8080", scheme="http"
    )

    return [
        get_city_name(geolocator.reverse, lat, lon)
        for (lat, lon) in (df[["latitude", "longitude"]].values)
    ]


def get_city_name(reverse, lat, lon):
    location = reverse(f"{lat}, {lon}", timeout=5)

    if location is None:
        print(f"Not Found: {lat}, {lon}")
        return None

    if location.raw is None:
        print(f"Not Found: {lat}, {lon}")
        return None

    address = location.raw.get("address")
    town = address.get("town")
    city = address.get("city")
    village = address.get("village")

    if town is not None:
        return town

    if city is not None:
        return city

    if village is not None:
        return village

    print("Unable to get city name:", address)
    return None


if __name__ == "__main__":
    coords = [
        (-12.13166666, -40.35416666),
        (-17.963056, -38.703333),
        (-51.94919444, -29.55475),
        (-40.49772222, -20.42841667),
    ]

    gl = Nominatim(
        user_agent="projeto_integrador_app", domain="localhost:8080", scheme="http"
    )
    for coord in coords:
        print(get_city_name(gl.reverse, *coord))

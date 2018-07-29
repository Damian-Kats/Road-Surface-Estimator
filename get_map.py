import requests
from io import BytesIO
from PIL import Image
import sys


GOOGLE_MAPS_API_KEY = 'AIzaSyAPFasRKxnFbM0FoDFikPNKT9QhCrwMPng'  # set to 'your_API_key'


def get_maps_image(ctr):
    zoom = '15'
    centre = ctr
    # Maximum size of map possible without premium plan is 640x640
    width = '265'
    height = '265'
    final = Image.new("RGB", (int(width), int(height)))
    # create custom Google Maps URL for the styled map
    url = 'https://maps.googleapis.com/maps/api/staticmap?key=' + GOOGLE_MAPS_API_KEY + '&center=' + centre + '&zoom='\
        + zoom + '&format=png&maptype=roadmap&style=element:labels%7Cvisibility:off&style=' \
        'feature:administrative%7Cvisibility:off&style=feature:administrative.land_parcel%7Cvisibility:' \
        'off&style=feature:administrative.neighborhood%7Cvisibility:off&style=feature:landscape%7Ccolor:' \
        '0x000000%7Cvisibility:on&style=feature:poi%7Cvisibility:off&style=feature:road%7Ccolor:0xffffff&' \
        'style=feature:road%7Celement:labels.icon%7Cvisibility:off&style=feature:transit%7Cvisibility:off' \
        '&style=feature:water%7Ccolor:0x000000&size=' + width + 'x' + height
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    im = Image.open(BytesIO(response.content))
    final.paste(im)

    return final

if __name__ == "__main__":
    centre = '-37.905953, 145.164633'
    result = get_maps_image(centre)
    result.show()
from GUI import run_gui


if __name__ == '__main__':
    run_gui()


# Development goals:
#   Load google map image into IDE (Done)
#   Convert image into binary colours (Done)
#   Count number of pixel per colour (Done)
#   Get percentage of road area in image (Done)
#   Work out map scale based on pixels and zoom level (Done, 3.769m per pixel at zoom 15)
#   Limit the initial map to be a 1km by 1km block (265x265 gives approx 1km squared map)
#   Add calculator/ability to save area values and sum up multiple areas sequentially
#   Rotate selected area on the map
#   Custom shapes

import math
from PIL import Image


def calculate_area(img):
    pixels = img.getdata()  # get all pixels in image
    black_pixels = 0
    total_pixels = len(list(pixels))  # total number of pixels in image
    for pixel in pixels:  # count number of black pixels in image
        if pixel == (0, 0, 0):
            black_pixels += 1
    road_ratio = 100 - ((black_pixels / total_pixels) * 100)  # calculate ratio of road in image
    #                                       latitude                                      Zoom
    metresPerPx = 156543.03392 * math.cos(-37.8989629260897 * math.pi / 180) / math.pow(2, 15)
    total_area = (metresPerPx * 265) ** 2
    road_area = round(total_area * (road_ratio / 100), 2)
    #km_dist = 1000 / metresPerPx
    #print("\nTotal pixels: ", total_pixels)
    #print("\nBlack pixels: ", black_pixels)
    #print("\nPercentage of image as road: ", road_ratio)
    #print("\nMetres per pixel: ", metresPerPx)
    #print("\nTotal area of map (m^2): ", total_area)
    #print("\nArea of roads (m^2): ", road_area)
    #print("\nImage width/height for 1km range in pixels: ", km_dist)
    #img.show()
    #img.save('output.png')
    return road_area

if __name__ == "__main__":
    test = Image.open("test_black.png")
    area = calculate_area(test)
    print(area)
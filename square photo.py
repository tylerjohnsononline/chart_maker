import chart_maker_library 
import cv2

def add_width_to_photo(photo, additional_photo_width):
  horizontal_compensation = chart_maker_library.make_vertically_long_border(photo,
                            thickness = additional_photo_width)
  new_photo = cv2.hconcat([photo,
                          horizontal_compensation])
  return new_photo


def add_height_to_photo(photo, how_much_height):
  vertical_compensation = chart_maker_library.make_horizontaly_long_border(photo=photo,
                            thickness = how_much_height)
  new_photo = cv2.vconcat([photo,
                         vertical_compensation])
  return new_photo


def make_a_photo_square_by_adding_blank_space(photo):
    original_dimensions = photo.shape
    vertical = original_dimensions[0]
    horizontal = original_dimensions[1]
    if vertical == horizontal:
      squared_photo = photo

    elif vertical > horizontal:
      # get a photo to append to the bottom to make up for the disparity
      additional_photo_width = vertical - horizontal
      # append to the bottom
      squared_photo = add_width_to_photo(additional_photo_width)

    elif vertical < horizontal:
      additional_photo_height = horizontal - vertical
      squared_photo = add_height_to_photo(photo=photo, how_much_height=additional_photo_height)

    return  squared_photo


path = "chart_maker\place_photo_to_be_charted_here\photo_to_become_chart.png"
photo = cv2.imread(path)

resulting_square = make_a_photo_square_by_adding_blank_space(photo)
cv2.imshow("window", resulting_square)
cv2.waitKey(0)
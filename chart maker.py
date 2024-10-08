from pathlib import Path
import os
from os import walk

import cv2
import chart_maker_library 


if __name__ == "__main__":
  pass
  picture = cv2.imread("chart_maker\place_photo_to_be_charted_here\photo.png")
  chart_maker_library.break_photo_into_grid(picture,5,5)
  # chart_maker_library.first_photo_chart(vertical_default=50,
  #                   horizontal_default=100,
  #                   darker_than_default=100)
  # user_given_values()



from pathlib import Path
import os
from os import walk

import cv2
import chart_maker_library 

def usable_chart_maker():
  path = "chart_maker\place_photo_to_be_charted_here\photo_to_become_chart.png"
  # picture = cv2.imread(path)
  print("how many vertical boxes?")
  print()
  vertical = int(input())
  print("how many horizontal boxes?")
  horizontal = int(input())
  chart_maker_library.first_photo_chart(path = path,
                                        vertical_default=vertical,
                    horizontal_default=horizontal,
                    darker_than_default=100)


if __name__ == "__main__":
  usable_chart_maker()



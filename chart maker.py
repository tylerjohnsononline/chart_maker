from pathlib import Path
import os
from os import walk



def get_photo_path(folder = "place_photo_to_be_charted_here"):
  mypath = folder
  f = []
  for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
  photo_name = f[0]
  
  final_path = f"{folder}/{photo_name}"
  return final_path



if __name__ == "__main__":
  get_photo_path()

  
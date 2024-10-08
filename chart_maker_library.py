import cv2 # for manipultaing photos
import os # for finding available photos
from matplotlib import pyplot as plt # for showing photos to the user
import numpy as np # for synthetically making photos
from PIL import Image # for changing photo colors

#break wapart and reaconstitute
def break_photo_into_grid(original_photo, # photo must be a png loaded in cv2, can't be a jpeg
                          pieces_vertical,
                          pieces_horizontal,):
  photo_grid = np.zeros((pieces_vertical, pieces_horizontal, 1),
                        dtype=type(original_photo))
  per_horizontal = original_photo.shape[0] / pieces_horizontal
  per_vertical = original_photo.shape[0] / pieces_vertical
  per_horizontal = round(per_horizontal)
  per_vertical = round(per_vertical)
  start_ii = 0
  start_jj = 0
  for ii in range(0, pieces_horizontal-0):
    for jj in range(0, pieces_vertical-0):
      start_ii = ii * per_horizontal
      start_jj = jj * per_vertical 

      #   the_chunk = of_image[x_start : x_start + psuedo_pixel_size[0],
  # y_start : y_start + psuedo_pixel_size[1]]

      # photo_piece = original_photo[ii*per_horizontal: +,
      #                              : +]
      photo_piece = original_photo[start_jj: start_jj+per_vertical,
                                   start_ii: start_ii+per_horizontal]


      photo_grid[jj, ii][0] = photo_piece

  
  grid_key = (pieces_vertical, pieces_horizontal)
  return photo_grid

def combine_grid_back_to_photo(grid):
  horizontal = grid.shape[0]
  vertical = grid.shape[1]
  
  for yy in range(vertical):

    for xx in range(horizontal):
      grid_spot = grid[xx, yy][0]
      if xx == 0: 
        horizontal_storage = grid_spot
      else:
        horizontal_storage = cv2.vconcat([horizontal_storage, grid_spot])

    if yy == 0:
      constructed_photo = horizontal_storage
    else: 
      constructed_photo = cv2.hconcat([constructed_photo, horizontal_storage])

  return constructed_photo


#alter photo color
def check_darker_than(photo, threshold):
  if threshold > photo[0][0][0]:
    result = True
  else:
    result = False
  return result

def check_lighter_than(photo, threshold):
  if threshold < photo[0][0][0]:
    result = True
  else:
    result =  False
  return result

def save_cv2_grayscale_piece(photo_to_save, name_to_save = 'working_spot_on_chart',
                           folder = "working_folder\\"):

  cv2.imwrite(f"{name_to_save}{folder}.png", photo_to_save)

def make_mono_grayscale_photo(vertical_size,
                              horizontal_size,
                              number_coresponding_gray = 150
                                ):
  import numpy as np

  height =  vertical_size
  width = horizontal_size

  blank_image = np.zeros((height, width, 3), np.uint16)
  
  #color it to be the corresponding gray in the keyword argument
  blank_image.fill(number_coresponding_gray)
  monocolor_photo = np.array(blank_image, dtype = 'uint8')
  # print("make_mono_grayscale_photo",monocolor_photo.shape)

  return monocolor_photo

def change_to_black_or_white(photo, threshold = 100,darker_than_or_equal_to = False,):
  # from PIL import Image
  # import cv2
  #from here it makes sense to extract into a function(remove scroll)\
  working_photo = 'working_spot_on_chart'
  path_to_store_photo_temporarily = "working_folder\\"
  # name_to_save = working_photo
  # folder = path_to_store_photo_temporarily
  # cv2.imwrite(f"{folder}{working}.png", photo)
  cv2.imwrite(f"{path_to_store_photo_temporarily}{working_photo}.png", photo)
  recolorable = Image.open(f'{path_to_store_photo_temporarily}{working_photo}.png')
  # print(f'path is: {path_to_store_photo_temporarily}{working_photo}.png')
  # print(recolorable)

  one_color_pixel = recolorable.convert('P', palette=Image.ADAPTIVE,
                                  colors=1)

  grayscale_pixel = one_color_pixel.convert('L', 
                                            palette=Image.ADAPTIVE,
                                            colors=1)

  grayscale_pixel.save(f'{path_to_store_photo_temporarily}{working_photo}gray.png',"PNG")
  gray_pre_threshold_pixel = cv2.imread(f'{path_to_store_photo_temporarily}{working_photo}gray.png')
  # print("gray pixel shape:",gray_pre_threshold_pixel.shape)
  #to here looks like it makes sense to extract into a function
  
  vertical_size = gray_pre_threshold_pixel.shape[0] 
  horizontal_size = gray_pre_threshold_pixel.shape[1]

  if darker_than_or_equal_to is True:
    # if check_darker_than(gray_pre_threshold_pixel, threshold): 
      pass
  elif darker_than_or_equal_to is False:
    if check_lighter_than(gray_pre_threshold_pixel, threshold):
      monocolor_image = make_mono_grayscale_photo(vertical_size,
                                                  horizontal_size, 
                                                  250)
    else:
      monocolor_image = make_mono_grayscale_photo(vertical_size,
                                                  horizontal_size, 
                                                  0)
  # show_photo(monocolor_image)
  return monocolor_image  
  
  # save_cv2_grayscale_piece(photo, name_to_save = 'working_spot_on_chart',
  #                          folder = "working_folder\\")

def make_monocolor_grayscale_in(grid, darkness_level):
  for ii in range(0, grid.shape[1]):
    for jj in range(0, grid.shape[0]):
      grid_spot = grid[jj, ii][0]
      # print("1")
      # show_photo(grid_spot)
      black_or_white_spot = change_to_black_or_white(grid_spot, threshold=darkness_level) # broken
      grid[jj, ii][0] = black_or_white_spot
  return grid


#border
def make_vertically_long_border(photo, 
                                thickness = 10,
                                number_coresponding_gray = 150
                                ):
  import numpy as np

  height = photo.shape[0] #here
  width = thickness #and flip height and width/s asignment parameters

  blank_image = np.zeros((height, width, 3), np.uint8)
  
  #color it to be the corresponding gray in the keyword argument
  blank_image.fill(number_coresponding_gray)
  matching_vertical_border = np.array(blank_image, dtype = 'uint8')

  return matching_vertical_border
def make_horizontaly_long_border(photo, 
                                thickness = 10,
                                number_coresponding_gray = 150
                                ):
  import numpy as np

  height =  thickness
  width = photo.shape[1] 

  blank_image = np.zeros((height, width, 3), np.uint8)
  
  #color it to be the corresponding gray in the keyword argument
  blank_image.fill(number_coresponding_gray)
  matching_horizontal_border = np.array(blank_image, dtype = 'uint8')
  

  return matching_horizontal_border
"the border doubles in thickness so set it in the low single didgets"
border_thickness = 5
"""
how dark the border is. black is 0, white is 255
gray is everything in between
"""
hue = 100
def put_a_border_around_the_photo(photo,
                              thickness = border_thickness,
                              level_of_gray = hue
                              ):
  vertical_border = make_vertically_long_border(photo,
                                                thickness,
                                                level_of_gray)
  left_bordered = cv2.hconcat([vertical_border,
                                photo])
  sides_bordered = cv2.hconcat([left_bordered,
                                vertical_border])
  
  
  horizontal_border = make_horizontaly_long_border(sides_bordered,
                                                   thickness,
                                                   level_of_gray)
  top_bordered = cv2.vconcat([horizontal_border,
                              sides_bordered])
  bottom_bordered = cv2.vconcat([top_bordered,
                                 horizontal_border])
  
  whole_photo_bordered = bottom_bordered
  return whole_photo_bordered

def border_photos_in(grid):
  for ii in range(0, grid.shape[1]):
    for jj in range(0, grid.shape[0]):
      grid_spot = grid[jj, ii][0]
      bordered_spot = put_a_border_around_the_photo(grid_spot)
      grid[jj, ii][0] = bordered_spot
  return grid

def make_chart_of(photo, horizontal = 4, vertical = 3, darker_than = 50):
  # change_to_black_or_white(photo, threshold = 100,darker_than_or_equal_to = False,):

  broken_photo_into_grid = break_photo_into_grid(photo,
                                                 vertical,
                                                 horizontal,)
  grayed = make_monocolor_grayscale_in(broken_photo_into_grid, darkness_level = darker_than)
  bordered_and_grayed = border_photos_in(grayed)
  rejoined_bordered_photo = combine_grid_back_to_photo(bordered_and_grayed)

  chart = rejoined_bordered_photo
  return chart

def save_chart_in(chart,
                  folder_to_save_in = "test_photos\\glacier_photo",
                  file_name = "testing_break_apart"):
  cv2.imwrite(f"{folder_to_save_in}\\{file_name}.png", chart)


def interactive_example_glacier_photo():
  relative_path = "test_photos\glacier_photo\public_domain_glacier_mountains.jpg"
  saved_in_folders = cv2.imread(relative_path)
  print("type number of pieces vertical")
  vertical = int(input())
  print("type number of pieces horizontal")
  horizontal = int(input())
  grid = break_photo_into_grid(original_photo = saved_in_folders,
                               pieces_horizontal=horizontal,
                               pieces_vertical=vertical,)
  print(grid.shape)

def example_glacier(horizontal_glacier, vertical_glacier):
  glacier_path = "test_photos\glacier_photo\public_domain_glacier_mountains.jpg"
  glacier_png = cv2.imread(glacier_path)
  glacier_chart = make_chart_of(photo = glacier_png,
                                 horizontal = horizontal_glacier, 
                                 vertical = vertical_glacier,
                                 darker_than = 50)
  save_chart_in(chart = glacier_chart,
                folder_to_save_in = "test_photos\glacier_photo",
                file_name = "testing_break_apart")

def get_first_path_from_user_original_folder(): 
  user_folder_path = "user_photos\\user_original\\"
  files = os.listdir(user_folder_path)
  for file in files[:]:
    if file.endswith(".png") or file.endswith("jpg") or file.endswith("jpeg"):
      file_name = file
      photo_path = user_folder_path + file_name
      return photo_path
  print("no photos in user_original folder")
  return

def save_user_chart(chart):
  destined_path = "user_photos\\chart_destination"
  finished_chart = "finished_chart"
  save_chart_in(chart,
                folder_to_save_in = destined_path,
                file_name = finished_chart)

def first_photo_chart(path,
                      vertical_default = 3, 
                      horizontal_default = 4, 
                      darker_than_default = 50):
  # def make_chart_of(photo, horizontal = 4, vertical = 3, darker_than = 50):
#   path = get_first_path_from_user_original_folder()
  # print(f"{get_first_path_from_user_original_folder()}")
  user_photo = cv2.imread(path)
  user_chart = make_chart_of(user_photo,
                             horizontal = horizontal_default,
                             vertical = vertical_default, 
                             darker_than = darker_than_default)
  save_user_chart(user_chart)

def user_given_values():
  horizontal_input = int(input())
  vertical_input= int(input())
  darkness_value_input = int(input())
  first_photo_chart(vertical_default=vertical_input,
                    horizontal_default=horizontal_input,
                    darker_than_default=darkness_value_input)

def view_looped_charts_in_vscode():
  for xx in range(0,255,50):
    first_photo_chart(18, 40, darker_than_default=xx)

def main():
  first_photo_chart(path = "chart_maker\place_photo_to_be_charted_here\photo.png",
                    vertical_default=50,
                    horizontal_default=100,
                    darker_than_default=100)
  # user_given_values()

if __name__ == "__main__":
  main()

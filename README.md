the bottom of this link shows an example of what can be done with the chart maker:
https://colab.research.google.com/github/tylerjohnsononline/chart_maker/blob/mspaint_ladybug_demo_in_colab/Chart_Maker_Colab_demo_ladybug_outline_Jupyter_Notebook.ipynb
### This is a prototype
I have had difficulty transfering from a colab notebook to command line runnable, partially to do with pathing difficulties. from this I have learned that I will need to manage the required data retrieval from pathing across systems separately first, then work with what is available.

a note: this version does not correct for distortion; as such, it's better to use a photo close in dimensions to the chart, and thus the final 
correcting for this is why square photo branch is made

### How To Get Started
```
1 open the goodle colab link
2 under user version hover over 7 cells hidden, then the circle play button and click on the play button
3 click run anyway when prompted, the alert warns you that the code was not written by google, as it was written by me, this is expected
4 under run this if you ant to uploaad a new photo click on the play butotn next to active_photo.get_photo()
5 click browse
6 then from your local files upload a photo
7 (optional) edit the number of pieces horizontally or verticcally to break the photo into
8 click the play button under run this and the backend with different numbers if you want a different number of horizontal or vertical stitches
9 click the play button under the backend
10 (optional) if you want to see your uploaded photo: click the play button next to show_photo(image)
11 (optional) if you want some example previews, click the playbutton next to minimum,
   11b  then click show code which is under
12 click the play button next to darkness_lv
13 (optional) change the darkness level if you want more dark places to show up in the final chart
14 click the play button next to bordered_preview to see the final result
15 right click on the image of the chart to copy or download it directly from this notebook
```
running this command
```
python chart_maker\\chartmaker.py
```
### Why
Photos take time to turn into a knitting and crafts project.

First you have to make a map or chart of what colors to put where.

This project was started to make this easier.

##### The Story
For my second project I wanted to do a project which solved a real problem for someone, something that saved time and made things easier for users so I asked a friend what something they wished existed.

That friend told me many knitters have photos in their galleries which they want to turn into a project.

In order to do so the photo must be made into a grid of what type of thread to use where(these can be referred to as stitch charts) before they can be knit or otherwise put together.

### What It Can Do
In its current version it can break up a photo into roughly as many pieces as you tell it to. uou have to change the code manually to do this as the code is now

This project can be used to get an idea of what a project might look like
### What It Can't Do
Since the number of stitches is incorrect, it can't be used out of the box to make a knitting chart yet

The relative size of the pieces the photo is broken up into is not maintained.

### There Is Always Room For Improvement
##### Because This Is A Prototype I Have Some Best Practices That I Am Fixing And Improving
There are too many global variables

In addition there are unused functions and underutilized classes

Currently this notebook can be run in Google Colaboratory(Colab) and not elsewhere, so minor changes need to be made to let it run on a local computer

##### bugs
When you change the number of pieces to break a photo into to be to high(more than like 5-10 in one dimension) the number of rectangles the photo is divided into is incorrect, usually off from one to three 

When making a grid that does not have an equal number of x and y boxes, the resulting image stretches.
It is believed this happens because more borders are around the pieces along the axis with more boxes

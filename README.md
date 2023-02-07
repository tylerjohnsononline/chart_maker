
### This is a prototype
### why
Photos take time to turn into a knitting and crafts project.

First you have to make a map or chart of what colors to put where.

This project was started to make this easier.

##### the story
For my second project I wanted to do a project which solved a real problem for someone, something that saved time and made things easier for users so I asked a friend what something they wished existed.

That friend told me many knitters have photos in their galleries which they want to turn into a project.

In order to do so the photo must be made into a grid of what type of thread to use where(these can be referred to as stitch charts) before they can be knit or otherwise put together.

### what it can do
In its current version it can break up a photo into roughly as many pieces as you tell it to. uou have to change the code manually to do this as the code is now

This project can be used to get an idea of what a project might look like
### what it can't do
Since the number of stitches is incorrect, it can't be used out of the box to make a knitting chart yet

The relative size of the pieces the photo is broken up into is not maintained.

### there is always room for improvement
##### because this was a prototype I have some best practices that I am fixing and improving
There are too many global variables

In addition there are unused functions and underutilized classes

Currently this notebook can be run in Google Colaboratory(Colab) and not elsewhere, so minor changes need to be made to let it run on a local computer

##### bugs
When you change the number of pieces to break a photo into to be to high(more than like 5-10 in one dimension) the number of rectangles the photo is divided into is incorrect, usually off from one to three 

When making a grid that does not have an equal number of x and y boxes, the resulting image stretches.
It is believed this happens because more borders are around the pieces along the axis with more boxes

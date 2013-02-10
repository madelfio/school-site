Title: Images Cheat-Sheet
Date: 2013-02-08 13:10
Author: Marco D. Adelfio
Summary: A cheat-sheet for working with images from the Linux command line.
Category: Notes

###Read image information (size, encoding information)

    :::console
    $ file example.png
    $ identify example.png  # (also works with jpegs)

###Resize image

    :::console
    $ convert example.png -resize 200x200 example.png  # resize to 200x200 pixels
    $ convert example.png -resize 200 example.png  # resize width to 200, preserving aspect ratio
    $ convert example.png -resize x200 example.png  # resize height to 200, preserving aspect ratio

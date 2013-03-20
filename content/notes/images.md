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

Resize to 200x200 pixels.

    :::console
    $ convert example.png -resize 200x200 example.png

Resize width to 200, preserving aspect ratio.

    :::console
    $ convert example.png -resize 200 example.png

Resize height to 200, preserving aspect ratio.

    :::console
    $ convert example.png -resize x200 example.png

### Crop image

Crop to 100x100 pixels, starting from pixel (5, 5), then resize canvas to
match result.

    :::console
    $ convert example.png -crop 100x100+5+5 +repage example.png

### Resize and crop from center

This is helpful if you want a thumbnail of a certain size, regardless of the
original aspect ratio ([doc](http://www.imagemagick.org/script/command-line-processing.php?ImageMagick=45bcl1a3agvbinon3bgbll7l16#geometry)).

    :::console
    $ convert example.jpg -resize 200x100^ -gravity center \
                          -crop 200x100+0+0 +repage example.jpg

### Add border

Add gray border, 1 pixel wide.

    :::console
    $ convert example.png -border 1 -bordercolor gray example.png

####Updates

*3/20/13* - Added cropping and border examples

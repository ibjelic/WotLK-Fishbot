# WotLK-Fishbot

Fishbot made in python using image recongition, no injections. 
(You will not be able to use computer, while this is working, it requires to control your mouse)


Best works with UI off (alt + z) and zoomed in first person, but it should work also with UI, depends mostly on your addons.

***Works fine on any image quality as I tested and any resolution, but it is using resolution of world of warcraft window, so you must either use it full screen, or align the window to the top left corner!***

Could work on any expansion, but tested and 'written' for wotlk.

## Setup

Python version used: 3.10.4 (Tested and works on py 3.11)

Install libraries:
```
pip install -r requirements.txt
```
if it still gives errors about libraries try instaling Pillow:
```
pip install pil
```

## How to use?
*Use at your own risk.*

```
python fishy.py
```

It's not detectable, since it emulates your mouse. But afk player fishing, not that hard to notice.


## How does it work

First of all, set macro on keybind 1:

```
/cast [nochanneling]  Fishing
```
This is used, so we dont cast over previous.



It takes fast screenshots, locates fishing blob using image 'Untitled.png' for comparison. You can always replace image of a blob for yours, if its struggling to find it. (Since the blob image has background, it will struggle for example in Undercity where the water is green)

After it locates the blob, it watches for movement (by Y axis)

line 86
```
if abs(sum(prev_y)/len(prev_y)-self.y)>3 and abs(sum(prev_x)/len(prev_x)-self.x)<5: blob_moved = True 
```
Treshold is 3 pixels for Y axis (it compares relative to average of last 3 screenshots), X axis has treshold so if it's a new cast, it doesnt jump right into it.
You can play around with treshold for Y axis if it doesnt work well.

line 93
```
if abs(sum(prev_x)/len(prev_x)-self.x)>3: self.cast_fishing()
```
If there is no blob, it will detect random coordinates, so this will recast it and process goes on. Also this won't cause any errors for recasting, because of the macro "[nochanneling]" 

I didn't implement any mechanisam to stop fishy, method I used to stop is, open start menu with Windows key, it crashes the program.

Program outputs coordinates of blob with every frame it takes, and outputs splash if it thinks there's a splash.



## Success rate?
Well for me its around 70%, but i've only used it in Northrend. 
There are missclicks sometimes, sometimes it doesnt detect movement of the blob. 
*If you want to fix this, you can use sound detection instead of blob movement. Also you can use some better blob locating alghoritm than mine*

In reality it's 0-80% depends on zone, if anything is running into frame and etc. For my purpose it leveled me from 375 to 450 in ~4 hours.


Happy fishing!




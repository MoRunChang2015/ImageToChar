# ImageToChar
Transform a image into char text using PIL

### Environment
+ **Ubuntu** 16.04 LTS
+ python 2.7.12


### Usage
1. Install **environment**
```
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev
sudo apt-get libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
sudo pip install pillow
sudo pip install docopt
```
2. Show help message

+ normal char

```
python src/ImageToChar.py -h
```

+ colored char

```
python src/ImageToColoredChar.py -h
```

3. Transform a image

+ normal char

```
python src/ImageToChar.py <PATH_TO_IMAGE>
```

+ colored char

'''
python src/ImageToColoredChar.py <PATH_TO_IMAGE> -c [ --hide ] [ -b ] [ --contrast=<factor> ]
'''

### Example

```
python src/ImageToChar.py images/ascii_dora.png --width 80 --height 60
```

**output**

![output](https://github.com/MoRunChang2015/ImageToChar/blob/master/data/example.png)

```
python src/ImageToColoredChar.py images/nyan.png --contrast=2.0 -c --hide
```

**origin**

![origin](https://github.com/MoRunChang2015/ImageToChar/blob/master/images/nyan.png)

**output**

![output](https://github.com/MoRunChang2015/ImageToChar/blob/master/data/example2.png)

```
python src/ImageToColoredChar.py images/coco.jpg --contrast=2.0 -c --hide
```

**origin**

![origin](https://github.com/MoRunChang2015/ImageToChar/blob/master/images/coco.jpg)

**output**

![output](https://github.com/MoRunChang2015/ImageToChar/blob/master/data/example3.png)


### Reference
+ [Python 图片转字符画](https://www.shiyanlou.com/courses/370/labs/1191/document)
+ [Python 3 图像转彩色字符画](https://www.shiyanlou.com/courses/673)

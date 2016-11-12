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
```
2. Show help message
```
python src/ImageToChar.py -h
```

3. Transform a image
```
python src/ImageToChar.py <PATH_TO_IMAGE>
```

### Example
```
python src/ImageToChar.py images/ascii_dora.png --width 80 --height 60
```
**output**


### Reference
+ [Python 图片转字符画](https://www.shiyanlou.com/courses/370/labs/1191/document)

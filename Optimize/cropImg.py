import cv2
import numpy
from matplotlib import pyplot as plt
import os
from PIL import Image

src_folder = "."
tar_folder = "tar"
backup_folder = "backup"

def isCrust(pix):
    return sum(pix) < 25

def xCheck(img, x, step = 50):
    count = 0
    height = img.size[1]
    for y in range(0, height, step):
        if isCrust(img.getpixel((x, y))):
            count += 1
        if count > height / step / 2:
            return True
    return False

def yCheck(img, y, step = 50):
    count = 0
    width = img.size[0]
    for x in range(0, width, step):
        if isCrust(img.getpixel((x, y))):
            count += 1
        if count > width / step / 2:
            return True
    return False

def boundaryFinder(img,crust_side,core_side,checker):
    '''
    :param img: the image whose boundary we need
    :param crust_side: outside of which is crust
    :param core_side: inside of which is picture we really want
    :param checker: xCheck or yCheck
    :return: the boundary co-value of Cartesian coordinates we found
    '''
    if not checker(img,crust_side):
        return crust_side
    if checker(img,core_side):
        return core_side

    '''
    Use binary search to find the crust boundary
    '''
    mid = (crust_side + core_side) / 2
    while  mid != core_side and mid != crust_side:
        if checker(img,mid):
            crust_side = mid
        else:
            core_side = mid
        mid = (crust_side + core_side) / 2
    return core_side

def handleImage(image):
    '''
    the input parameter is read by cv2.imread
    which need to be transformed into PIL.Image
    '''
    # img = Image.open(os.path.join(src_folder,filename))
    img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if img.mode != "RGB":
        img = img.convert("RGB")

    width, height = img.size

    '''
    work out the four points' co-value of result rectangle
    '''
    left = boundaryFinder(img, 0, width/2, xCheck)
    right = boundaryFinder(img, width-1, width/2, xCheck)
    top = boundaryFinder(img, 0, height/2, yCheck)
    bottom = boundaryFinder(img, height-1, width/2, yCheck)

    rect = (left,top,right,bottom)
    # print(rect)

    stitched = img.crop(rect)

    plt.imshow(stitched)
    plt.show()
    '''
    Change the result into cv2 format and return it
    '''
    stitched = cv2.cvtColor(numpy.array(stitched), cv2.COLOR_BGR2RGB)
    return stitched
    # stitched.save(os.path.join(filename),'PNG')

# if __name__ == '__main__':
#     main()
#     handleImage(os.path.abspath("..")+'/test/res_Pic/bug.jpg')

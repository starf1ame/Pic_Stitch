from PIL import Image
import os

def findMax(num1,num2):
    if (num1 > num2):
        return num1
    else:return num2

def resize(path1,path2):

    im_1 = Image.open(path1)
    im_2 = Image.open(path2)

    width_1,height_1 = im_1.size
    width_2,height_2 = im_2.size

    print(width_1,' ',height_1)
    print(width_2, ' ', height_2)

    if (width_1,height_1)==(width_2,height_2):
        return True
    else:
        W = findMax(width_1,width_2)
        H = findMax(height_1,height_2)
        print(W,' ',H)
        img_1 = im_1.resize((W, H), Image.ANTIALIAS)
        img_2 = im_2.resize((W, H), Image.ANTIALIAS)
        img_1.save(path1,quality=100)
        img_2.save(path2, quality=100)
        return True

# if __name__ == '__main__':
#     resize(os.path.abspath("..")+'/test/res_Pic/result_1.jpg',\
#            os.path.abspath("..")+'/test/res_Pic/result_2.jpg')

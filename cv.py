import numpy as np
import cv2
from PIL import Image

drawing = False #鼠标按下为真
mode = True #如果为真，画矩形，按m切换为曲线
ix,iy=-1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)


img = np.zeros((400,400),np.uint8) +255
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

def imageprepare():
    """
        This function returns the pixel values.
        The input is a png file location.
    """
    file_name = 'temp_image.png'
    im = Image.open(file_name).convert('L')
    im = im.resize((20, 20))
    p = Image.new('L', (28,28), (255))
    p.paste(im,(4,4,24,24))
    p.save("last_image.png")

    tv = list(p.getdata())  # get pixel values
    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    tva = np.reshape(tva, (28, 28))

    return tva

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m') :
        mode = not mode
    elif k == 13:
        cv2.imwrite('temp_image.png', img)
        result = imageprepare()
    elif k == 27:
        break
cv2.destroyAllWindows()
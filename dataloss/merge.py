import cv2
import numpy as np

base_image = cv2.imread("back_small.png")
# base_image = cv2.imread("back.jpg")
x_offset=y_offset=15

for x in range(1, 5):
    cv2.imwrite('./video/000_'+str(x)+'.png', base_image)

for x in range(1, 5):
    
    s_img = cv2.imread("./img/"+str(x).zfill(3)+".png")    

    l_img = base_image; # + np.random.normal(mean, std, base_image.shape)

    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

    cv2.imwrite('./video/'+str(x).zfill(3)+'_a.png', l_img)

    img = np.zeros([l_img.shape[0],l_img.shape[1],3],dtype=np.uint8)
    img.fill(255) # or img[:] = 255

    cv2.imwrite('./video/'+str(x).zfill(3)+'_b.png', img)
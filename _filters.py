# module imports
from skimage import io, img_as_float
import numpy as np
import cv2 as cv2


# importing image file as grey
img = img_as_float (io.imread("image/image.jpg", as_gray=True))


# defining our normalized kernels
mean_kernel = np.ones((5,5), np.float32 )/25

gaussian_kernel = np.array([[1/16, 1/8, 1/16],
                           [1/8, 1/4, 1/8],
                           [1/16, 1/8, 1/16]]
                           )
# edge detection vertical and horizontal filter
edge_detection_vertical = np.array([[-1,-2,-1],[0,0,0],[1,2,1]]) 
edge_detection_horizontal = np.array([[-1,0,1],[-2,0,2],[-1,0,1]]) 


# applying this to the image.
mean = cv2.filter2D(img, -1, mean_kernel, borderType = cv2.BORDER_CONSTANT)
gaussian = cv2.filter2D(img, -1, gaussian_kernel, borderType = cv2.BORDER_CONSTANT)
edge_detection = cv2.filter2D(img, -1, edge_detection_vertical, borderType = cv2.BORDER_CONSTANT)
edge_detection = cv2.filter2D(img, -1, edge_detection_horizontal, borderType = cv2.BORDER_CONSTANT)

cv2.imshow("Original", img)
cv2.imshow("gaussian", gaussian)
cv2.imshow("mean", mean)
cv2.imshow("edge detection", edge_detection)

cv2.waitKey(0)
cv2.destroyAllWindows();
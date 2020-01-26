import cv2
"""
https://stackoverflow.com/questions/49093729/remove-background-of-any-image-using-opencv/49098862

"""
# == Parameters
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0, 0.0, 1.0)  # In BGR format


class BackGroudRemove:
    def __init__(self, image, window_name="BackGroudRemove"):
        print("Background Remove Calling")
        self.image = image
        self.window_name = window_name

    def remove_background(self):
        pass

    def show_image(self, window_name=None):
        if not window_name:
            window_name = self.window_name
        cv2.imshow(window_name, self.image)
        cv2.waitKey(0)      # press any key to destroy window


if __name__ == '__main__':
    # -- Read image
    img = cv2.imread('images/couple.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bgr = BackGroudRemove(image=img)




    bgr.show_image(window_name="image")

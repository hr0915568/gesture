import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
import sched, time

cap = cv.VideoCapture(0)
numberOfFrameToUseToMergde = 4

frames_holder = []

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv.imshow('frame',frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()

#settings
#
# cap = cv.VideoCapture(0)
# while (True):
#      ret, frame = cap.read()
#      cv.imshow('frame', frame)
#      cv.waitKey(1)
#      # if cv.waitKey(1) & 0xFF == ord('q'):
#      #     break
# cap.release()
# cv.destroyAllWindows()
# exit()
#

#
def merge_frames(frames):
    global np

    first_frame = frames[0]
    frames.pop(0)
    for frame in frames:
            first_frame = np.concatenate((first_frame, frame), axis=1)

    return first_frame
#
#
def capture_frame():
    global cap, frames_holder, cv, numberOfFrameToUseToMergde
    ret, frame = cap.read()
    cv.waitKey(1)
    frames_holder.append(frame)
    if (ret != True):
        print("not capturing")
        return

    if len(frames_holder) == numberOfFrameToUseToMergde:
        # merge the frames;
        merged_frame = merge_frames(frames_holder)
        merged_frame = cv.cvtColor(merged_frame, cv.COLOR_BGR2GRAY)
        #merged_fram.e = cv.Canny(merged_frame, 100, 200)
        print(merged_frame.shape)
        cv.imshow('frame', merged_frame)
        frames_holder = []

    return frame
#
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    capture_frame()
    # do your stuff
    s.enter(0.15, 1, do_something, (sc,))

s.enter(0.15, 1, do_something, (s,))
s.run()
exit()
#

#
#
#
#
# images = []
# frameRate = cap.get(5) #frame rate
# tmp = []
#
# while(True):
#     frameId = cap.get(cv.CAP_PROP_FRAME_COUNT)  # current frame number
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # Our operations on the frame come here
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     if (frameId % math.floor(frameRate) == 0):

#
# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()

# img = cv2.imread('test.jpg', 0)
# edges = cv2.Canny(img, 100, 200)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#
# plt.show()
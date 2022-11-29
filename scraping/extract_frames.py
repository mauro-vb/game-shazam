import cv2
#print(cv2.__version__) # WE CAN HAVE DIFFERENT VERSIONS!

def extract_frames(pathIn:str, pathOut:str, ident:str):
    '''receives
    pathIn video file path
    pathOut to screenshots
    id from the video id list
    creates image files in pathOut folder'''

    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        try:
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*5000)) # each 5 seconds
            success,image = vidcap.read()
            print ('Reading frame: ', success)
            cv2.imwrite(pathOut + f"{ident}_frame%d.jpg" % count, image) # save frame as JPEG file
            count = count + 1
        except:
            continue

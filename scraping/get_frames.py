import cv2
#print(cv2.__version__) # WE CAN HAVE DIFFERENT VERSIONS!

def extract_frames(pathIn:str, pathOut:str, ident:str, gamename: str):
    '''receives
    pathIn video file path
    pathOut to screenshots
    id from the video id list
    creates image files in pathOut folder'''
    # print("got into extract frames")
    count = 1
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        try:
            # print("got into while, try")
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*15000)) # each 5 seconds
            success,image = vidcap.read()
            # print ('Reading frame: ', success)
            cv2.imwrite(pathOut + f"{ident}_frame%d.jpg" % count, image) # save frame as JPEG file
            count = count + 1

        except:
            continue

    print("---------------------\n")
    print(f"Finished generating images for '{gamename}' gameplay.\n")
    return count

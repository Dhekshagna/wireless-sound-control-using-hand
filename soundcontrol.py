#Importing the libraries
import cv2 
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

#To get the audio interface 
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


cap = cv2.VideoCapture(0)#capturing image froom laptop camera
hands = mp.solutions.hands.Hands()
connection = mp.solutions.drawing_utils#to get hand connections


while True:
    #Reading image and detecting the hand 
    success,img = cap.read()
    RGB_image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    output = hands.process(RGB_image)

    
    #When a hand is detected for every hand all the 21 land marks are found in terms of pixels and connected  
    if output.multi_hand_landmarks:
        for each_hand in output.multi_hand_landmarks:
            ldmrk_lst = []
            
            for index,ldmrk in enumerate(each_hand.landmark):
                h , w , c=img.shape
                cx , cy = int(ldmrk.x*w) ,int(ldmrk.y*h)
                ldmrk_lst.append([index , cx , cy])
            connection.draw_landmarks(img,each_hand,mp.solutions.hands.HAND_CONNECTIONS)

            
        if ldmrk_lst:
            #to get the landmarks of the tip of index and thumb
            a1 , a2 = ldmrk_lst[4][1], ldmrk_lst[4][2]
            b1 , b2 = ldmrk_lst[8][1], ldmrk_lst[8][2]
            cv2.circle(img,(a1,a2) ,7,(23,73,120),cv2.FILLED)
            cv2.circle(img,(b1,b2) ,7,(23,73,120),cv2.FILLED)
            cv2.line(img,(a1,a2),(b1,b2),(0,0,255))

            
            #To get the length btw index and thumb 
            lenth = math.hypot(b1-a1,b2-a2)
            print(lenth)

            
            #Length where the volume has to be 0
            if lenth<50:
                p1=(a1+b1)//2
                p2=(a2+b2)//2
                cv2.circle(img,(p1,p2) ,7,(23,73,120),cv2.FILLED)
                
                
        #Finding the range and mapping it with the length
        range_vol=volume.GetVolumeRange()
        minsound = range_vol[0]
        maxsound = range_vol[1]
        sound = np.interp(lenth, [50,250] ,[minsound,maxsound])

        
        #Soundbar inside the rectangle mapping
        soundbar = np.interp(lenth, [50,250] ,[400,150])

        
        #Showing volume in percentage by mapping with volume lenth 
        soundper = np.interp(lenth, [50,250] , [0,100])
        volume.SetMasterVolumeLevel(sound, None)

        
        #Creating a rectangle for the sound box
        cv2.rectangle(img, (50,150), (85,400), (0,0,255),3)
        cv2.rectangle(img, (50, int(soundbar)), (85,400), (126,111,250), cv2.FILLED)

        
        #To get the text on the image
        cv2.putText(img,str(int(soundper))+"%"   ,(10,100),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,3,(0,0,0))
    #Show the image    
    cv2.imshow("image",img)
    if cv2.waitKey(1) == ord('q'):#use q on the keyboard to quit from the code
        break
    

cap.release()
cv2.destroyAllWindows()



import cv2
from align_custom import AlignCustom
from face_feature import FaceFeature
from mtcnn_detect import MTCNNDetect
from tf_graph import FaceRecGraph
import argparse
import sys
import json
import time
import numpy as np
from tkinter import *
from tkinter import messagebox, filedialog, ttk
import mysql.connector as mysql
import datetime

TIMEOUT = 10 #10 seconds

def main(args):
    
    
    camera_recog();



def camera_recog():
    print("[INFO] camera sensor warming up...")
   
    con=mysql.connect(host="localhost",user="root",password="SaS@root1",database="sas")
    cursor=con.cursor()
    
    vs = cv2.VideoCapture(0); #get input from webcam
    detect_time = time.time()
    a = []
    currentDT = datetime.datetime.now()
    present= "Present"
    classid="BSCS"
    today = str(currentDT)
    while True:
        _,frame = vs.read();
        #you can certainly add a roi here but for the sake of a demo i'll just leave it as simple as this
        rects, landmarks = face_detect.detect_face(frame,80);#min face size is set to 80x80
        aligns = []
        positions = []

        for (i, rect) in enumerate(rects):
            aligned_face, face_pos = aligner.align(160,frame,landmarks[:,i])
            if len(aligned_face) == 160 and len(aligned_face[0]) == 160:
                aligns.append(aligned_face)
                positions.append(face_pos)
            else: 
                print("Align face failed") #log        
        if(len(aligns) > 0):
            features_arr = extract_feature.get_features(aligns)
            recog_data = findPeople(features_arr,positions)
            for (i,rect) in enumerate(rects):
                cv2.rectangle(frame,(rect[0],rect[1]),(rect[2],rect[3]),(255,0,0)) #draw bounding box for the face
                cv2.putText(frame,recog_data[i][0]+" - "+str(recog_data[i][1])+"%",(rect[0],rect[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)
                student = recog_data[i][0]
                
                if student not in a:
                    a.append(student)
                
        if 'Unknown' in a:
            a.remove('Unknown')
        print (a)
        cv2.imshow("Mark Attendance",frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("p"):
            break
    
    
    for i in a: 
        cursor.execute("INSERT INTO attendance (class,student,date,stat) values('"+classid+"','"+i+"','"+today+"','"+present+"')")

    
    cursor.execute("commit");
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Attendance","Attendance Marked Successfully")
    
    vs.release()
    cv2.destroyAllWindows()
    
    #root.destroy()
'''
facerec_128D.txt Data Structure:
{
"Person ID": {
    "Center": [[128D vector]],
    "Left": [[128D vector]],
    "Right": [[128D Vector]]
    }
}
This function basically does a simple linear search for 
^the 128D vector with the min distance to the 128D vector of the face on screen
'''
def findPeople(features_arr, positions, thres = 0.6, percent_thres = 70):
    '''
    :param features_arr: a list of 128d Features of all faces on screen
    :param positions: a list of face position types of all faces on screen
    :param thres: distance threshold
    :return: person name and percentage
    '''
    f = open('./facerec_128D.txt','r')
    data_set = json.loads(f.read());
    returnRes = [];
    for (i,features_128D) in enumerate(features_arr):
        result = "Unknown";
        smallest = sys.maxsize
        for person in data_set.keys():
            person_data = data_set[person][positions[i]];
            for data in person_data:
                distance = np.sqrt(np.sum(np.square(data-features_128D)))
                if(distance < smallest):
                    smallest = distance;
                    result = person;
        percentage =  min(100, 100 * thres / smallest)
        if percentage <= percent_thres :
            result = "Unknown"
        returnRes.append((result,percentage))
    return returnRes    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, help="Run camera recognition", default="camera")
    args = parser.parse_args(sys.argv[1:]);
    FRGraph = FaceRecGraph();
    MTCNNGraph = FaceRecGraph();
    aligner = AlignCustom();
    extract_feature = FaceFeature(FRGraph)
    face_detect = MTCNNDetect(MTCNNGraph, scale_factor=2); #scale_factor, rescales image for faster detection
    main(args);

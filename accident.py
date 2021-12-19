import os
import imutils
import dlib
import cv2
from imutils import face_utils
from scipy.spatial import distance
from utilities import eye_aspect_ratio, mouth_aspect_ratio


def _init_():
    eyethresh = 0.25
    mouththresh = 0.60
    frame_check_eye = 5
    frame_check_mouth = 5
    detect = dlib.get_frontal_face_detector()
    predict = dlib.shape_predictor("../model/shape_predictor_68_face_landmarks.dot")
    (lstart, lend) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
    (rstart, rend) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
    (mstart, mend) = face_utils.FACIAL_LANDMARKS_68_IDXS["mouth"]
    cap = cv2.VideoCapture(0)
    flag_eye = 0
    flag_mouth = 0
    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, height=800, width=1000)
        gray = cv2.cvtcolor(frame, cv2.COLOR_BGR2GRAY)
        subjects = detect(gray, 0)
        for subject in subjects:
            shape = predict(gray, subject)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[lstart:lend]
            rightEye = shape[rstart:rend]
            mouth = shape[mstart:mend]

            leftEar = eye_aspect_ratio(leftEye)
            rightEar = eye_aspect_ratio(rightEye)

            ear = (leftEar + rightEar) / 2.0

            leftEyehull = cv2.convexHull(leftEye)
            rightEyehull = cv2.convexHull(rightEye)

            mar = mouth_aspect_ratio(mouth)
            mouthhull = cv2.convexHull(mouth)

            cv2.drawContours(frame, [leftEyehull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyehull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [mouth], -1, (0, 255, 0), 1)
            cv2.putText(frame, "Eye Aspect Ratio:{}".format(ear), (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255),
                        2)
            cv2.putText(frame, "Mouth Aspect Ratio:{}".format(mar), (5, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 255, 255), 2)
            if mar > mouththresh:
                flag_mouth += 1
                if flag_mouth >= frame_check_mouth:
                    cv2.putText(frame, "**** SUBJECT IS YAWNING ****", (10, 370), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                (0, 0, 225), 2)
            else:
                flag_mouth = 0
                if ear < eyethresh:
                    flag_eye += 1
                    if flag_eye >= frame_check_eye:
                        cv2.putText(frame, "**** SUBJECT IS YAWNING ****", (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                    (0, 0, 225), 2)
                else:
                    flag_eye = 0
        cv2.inshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
    cap.stop()import os
import imutils
import dlib
import cv2
from imutils import face_utils
from scipy.spatial import distance
from utilities import eye_aspect_ratio,mouth_aspect_ratio

def _init_():
    eyethresh=0.25
    mouththresh=0.60
    frame_check_eye=5
    frame_check_mouth=5
    detect=dlib.get_frontal_face_detector()
    predict=dlib.shape_predictor("../model/shape_predictor_68_face_landmarks.dot")
    (lstart,lend)=face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
    (rstart,rend)=face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
    (mstart,mend)=face_utils.FACIAL_LANDMARKS_68_IDXS["mouth"]
    cap=cv2.VideoCapture(0)
    flag_eye=0
    flag_mouth=0
    while True:
        ret,frame=cap.read()
        frame=imutils.resize(frame,height=800,width=1000)
        gray=cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
        subjects=detect(gray,0)
        for subject in subjects:
            shape=predict(gray,subject)
            shape=face_utils.shape_to_np(shape)

            leftEye=shape[lstart:lend]
            rightEye=shape[rstart:rend]
            mouth=shape[mstart:mend]

            leftEar=eye_aspect_ratio(leftEye)
            rightEar=eye_aspect_ratio(rightEye)

            ear=(leftEar+rightEar)/2.0

            leftEyehull=cv2.convexHull(leftEye)
            rightEyehull=cv2.convexHull(rightEye)

            mar=mouth_aspect_ratio(mouth)
            mouthhull=cv2.convexHull(mouth)

            cv2.drawContours(frame,[leftEyehull],-1,(0,255,0),1)
            cv2.drawContours(frame,[rightEyehull],-1,(0,255,0),1)
            cv2.drawContours(frame,[mouth],-1,(0,255,0),1)
            cv2.putText(frame,"Eye Aspect Ratio:{}".format(ear),(5,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)
            cv2.putText(frame,"Mouth Aspect Ratio:{}".format(mar),(5,80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)
            if mar>mouththresh:
                flag_mouth +=1
                if flag_mouth>=frame_check_mouth:
                    cv2.putText(frame,"**** SUBJECT IS YAWNING ****",(10,370),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,225),2)
            else:
                flag_mouth=0
                if ear < eyethresh:
                    flag_eye+=1
                    if flag_eye >= frame_check_eye:
                        cv2.putText(frame,"**** SUBJECT IS YAWNING ****",(10,400),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,225),2)
                else:
                    flag_eye=0
        cv2.inshow("Frame",frame)
        key=cv2.waitKey(1)&0xFF
        if key==ord("q"):
            break
    cv2.destroyAllWindows()
    cap.stop()vv
import cv2
import numpy as np
cap = cv2.VideoCapture(0) #0 means capture from the first camera device
frames = []
gap = 5 # capture a frame every 5 seconds
frame_count = 0

while True:
    return_value, frame = cap.read() #reading the frame variable from cap
    if not return_value:# if not return_value, break the loop
        break
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert the frame to grayscale
    frames.append(gray) # append the grayscale frame to the frames list

    if len(frames)>gap+1: # if the length of frames is greater than gap
        frames.pop(0) # remove the first frame from the list
    cv2.putText(frame, f"{frame_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if len(frames) == gap + 1: # if the length of frames is equal to gap + 1
        diff = cv2.absdiff(frames[0], frames[-1]) # calculate the absolute difference between the first and last frame
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY) # apply a binary threshold to the difference image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # find contours in the thresholded image

        for contour in contours: # iterate through each contour
            if cv2.contourArea(contour) < 5000: # if the area of the contour is less than 500 pixels, ignore it
                continue
            (x, y, w, h) = cv2.boundingRect(contour) # get the bounding rectangle for the contour
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) # draw a rectangle around the detected motion
        motion = any (cv2.contourArea(contour) >= 500 for contour in contours) # check if any contour has an area greater than or equal to 500 pixels
        #gives true/false if motion is detected or not
        if motion:
            cv2.putText(frame, "Motion detected", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) # display "Motion detected" on the frame
            # cv2.imwrite(f"motion_frame_{frame_count}.jpg", frame) # save the frame with motion detected
            # print(f"Saved: motion_frame_{frame_count}.jpg") # print the saved frame name
        frame_count += 1 # increment the frame count
    cv2.imshow("Motion Detection", frame) # display the frame with motion detection

    if cv2.waitKey(1) & 0xFF in (27, ord('q')): # if Esc or 'q' is pressed, break the loop
        break

cap.release() # release the video capture object
cv2.destroyAllWindows() # close all OpenCV windows

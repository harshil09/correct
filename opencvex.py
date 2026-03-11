import cv2



#image=cv2.imread(r"C:\Users\harsh\OneDrive\Desktop\image.jpg")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()




#gray=cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
#cv2.imshow("My Image", gray) #show image
#cv2.waitKey(0) #wait for the key to be pressed
#cv2.destroyAllWindows() # closes all windows
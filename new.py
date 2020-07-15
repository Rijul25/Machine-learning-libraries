import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")



while True:
	ret,frame = cap.read()
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if ret == False:
		continue

	faces = face_cascade.detectMultiScale(gray_frame,1.3,5) 

	for(x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow("Video frame",frame)
	

	#wait for user input - q , then you will stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF #here cv2.waitkey gives us a 32 bit integer 
	# usko 0xff ke saath and karna hai. 0xff = 8 ones. to 32 bit integer and with 8 bit integer
	# to bas humei last ke 8 ones milenge.
	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

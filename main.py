import cv2 
import face_recognition

camera = cv2.VideoCapture(0) 
counter=0

def getFace(img):
    counter=0
    face_locations = face_recognition.face_locations(img)
    
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face = img[top:bottom, left:right]
        cv2.imwrite(r"yuz.png", face)
        counter +=1
    return counter


def faceKarsilastir():            
    h_image = face_recognition.load_image_file(r"hakan\1.png")
    c_image = face_recognition.load_image_file("yuz.png")

    height, width, _ = h_image.shape
    cheight, cwidth, _ = c_image.shape

    face_location = (0, width, height, 0)
    cface_location = (0, cwidth, cheight, 0)

    h_encodings = face_recognition.face_encodings(img, known_face_locations=[face_location])
    c_encodings = face_recognition.face_encodings(img, known_face_locations=[cface_location])
    if len(h_encodings) > 0 and len(c_encodings) > 0:
        h_encodings = h_encodings[0]
        c_encodings = c_encodings[0]
    else:
       print("No faces found in the image!")


    result = face_recognition.compare_faces([h_encodings],c_encodings)
    if result[0] == True:
        print("eşleşti:) ")
    else:
        print("yohhh : ")
      
while True:
    ret, img = camera.read()
    counter = getFace(img)
    
    if counter != 0: break 
    
    #cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break  

faceKarsilastir()


camera.release() # Close the window 
cv2.destroyAllWindows() # De-allocate any associated memory usage 
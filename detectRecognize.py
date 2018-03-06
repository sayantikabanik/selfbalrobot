import face_recognition
import os
import glob
#source="/home/sayantika/namedlist"
#dest="/home/sayantika/unnamedlist"
#source_location=os.path.dirname(face_recognition.load_image_file("/home/sayantika/namedlist"))
#dest_location=os.path.dirname(face_recognition.load_image_file("/home/sayantika/unnamedlist"))
x=0

for img in glob.glob('/home/sayantika/namedlist/*.jpg'):
	sourceimg=face_recognition.load_image_file(img)
	source_face_encoding = face_recognition.face_encodings(sourceimg)[0]
	for img2 in glob.glob('/home/sayantika/unnamedlist/*.jpg'):
		
		#print (source_face_encoding)
		destimg=face_recognition.load_image_file(img2)
		dest_face_encoding = face_recognition.face_encodings(destimg)[0]
		#print (dest_face_encoding)
		match = face_recognition.compare_faces(source_face_encoding, [dest_face_encoding])
		print(match)
		x=x+1
		print(x)
		

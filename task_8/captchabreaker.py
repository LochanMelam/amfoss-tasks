from PIL import Image
import pytesseract #gets text from image
captcha = Image.open('/home/lochan_melam28/Downloads/cap.png') #opens the image from given path
breaker = pytesseract.image_to_string(captcha) #gets text from the selected png and stores the text
result=0
a=int(breaker[0]) #by default the text is in string format so we use int function to convert into integer form
b=breaker[-2]
c=int(breaker[-1])
if b=="+":
	result=a+c
elif b=="-":
	result=a-c
elif b=="*":
	result=a*c
elif b=="/":
	result=a/c
else:
	result="can't be done"
print(result)  
	

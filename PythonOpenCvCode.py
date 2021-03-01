from pyzbar.pyzbar import decode
import cv2
used_codes=[];
goods={}
indf=0
while True:
	print("1 To add")
	print("2 To sell")
	print("3 To See")
	choice=int(input("Enter your choice:"))
	if(choice==1):
		cap=cv2.VideoCapture(0)
		cap.set(3,640)#3---Width
		cap.set(4,480)#4---Height
		
		while True:
			ret,frame=cap.read()
			for code in decode(frame):
				
					barcode=code.data.decode('utf-8')
					q=int(input("Enter the quantity"))
					i=0
					name=input("Enter the name of this product:")
					goods[name]=barcode
					for i in range(q):
						used_codes.append(barcode)

			cv2.imshow("Img",frame)
			if cv2.waitKey(1)==ord('q'):
				break;
		cap.release()
	if choice==2:
		u=0
		cap=cv2.VideoCapture(0)
		cap.set(3,640)#3---Width
		cap.set(4,480)#4---Height
		camera=True
		while camera==True:
			ret,frame=cap.read()
			for code in decode(frame):
				
					barcode=code.data.decode('utf-8')
					if len(used_codes)!=0:
						indf=0
						while((used_codes[indf]!=barcode) and (indf<len(used_codes)-1)):
							indf=indf+1
						if indf>=len(used_codes):
							print("Sorry this item does not exist")
						else:
						
							del used_codes[indf]
					else:
						print("Sorry this item does not exist")
					camera=False
					indf=0
			cv2.imshow("Img",frame)
			if cv2.waitKey(1)==ord('q'):
				break;
		cap.release()
	if choice==3:
		for key, value in goods.items():
			quantity=0;
			for i in range(len(used_codes)):
				if value==used_codes[i]:
					quantity=quantity+1
			print(f"There is {quantity} of {key}")
	if choice==0:
		break
cap.release()
cv2.destroyAllWindows()

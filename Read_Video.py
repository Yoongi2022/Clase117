import cv2

vid=cv2.VideoCapture("instasave.MP4")
if(vid.isOpened()==False):
    print("No se pudieron leer los datos")
height=int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width=int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps=int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

out=cv2.VideoWriter("boxing.mp4",cv2.VideoWriter_fourcc(*"DIVX"),30,(width,height))

while(True):
    ret,frame=vid.read() #Ret=Número boleano
    cv2.imshow("webcam",frame)
    out.write(frame)

    if cv2.waitKey(1)==32:
        break
vid.release()
out.release()
#cv2.destroyAllWindows()
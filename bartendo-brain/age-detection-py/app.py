import cv2
from PIL import ImageTk, Image
from tkinter import Tk, Label

window = Tk()

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

result, img = camera.read()

if result:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    print(img)
    
    img_pil = Image.fromarray(img)
    img_pil.save("assets\\test.png")
    
    img_tk = ImageTk.PhotoImage(img_pil)
    
    panel = Label(window, image=img_tk)
    panel.pack(side="bottom", fill="both", expand="yes")
    
    panel.img_tk = img_tk

else:
    print("Failed to capture image from camera.")

window.mainloop()

camera.release()
cv2.destroyAllWindows()

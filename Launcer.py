from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import *
import PIL
from PIL import Image,ImageTk,ImageFilter

class MainWindow:
    def  __init__(self,master):
        image=Image.open("1.jpg")
        size = width, height = 200, 200
        resize_image=image.resize(size)
        photo = ImageTk.PhotoImage(resize_image)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.place(x=200,y=100)

        image=Image.open("2.jpg")
        size = width, height = 200, 200
        resize_image=image.resize(size)
        photo = ImageTk.PhotoImage(resize_image)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.place(x=400,y=100)
        image=Image.open("3.jpg")
        size = width, height = 200, 200
        resize_image=image.resize(size)
        photo = ImageTk.PhotoImage(resize_image)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.place(x=600,y=100)
        image=Image.open("4.jpg")
        size = width, height = 200, 200
        resize_image=image.resize(size)
        photo = ImageTk.PhotoImage(resize_image)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.place(x=200,y=300)
        image=Image.open("5.jpg")
        size = width, height = 200, 200
        resize_image=image.resize(size)
        photo = ImageTk.PhotoImage(resize_image)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.place(x=400,y=300)
        image=Image.open("6.jpg")
        size = width, height = 200, 200
        resize_image=image.resize(size)
        photo = ImageTk.PhotoImage(resize_image)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.place(x=600,y=300)
        imageButton=ttk.Button(master,text="Click here to select Image",command=self.browse);
        imageButton.place(x=400,y=520)
        proceed_button=ttk.Button(root,text='Click here to proceed!',command=self.open_new_window)
        proceed_button.place(x=400,y=550)


    def browse(self):
        root.filename = filedialog.askopenfilename()
        storeImage=root.filename
        self.size=width,height=500,500
        self.image=Image.open(storeImage)
        got_image=self.image.resize(self.size)
        self.photo=ImageTk.PhotoImage(got_image)
        #label=Label(image=photo)
        #label.image=photo
        #label.place(x=100,y=450) 


    def open_new_window(self):    	
        newwindow = Toplevel(root)
        newwindow.title("Join")
        newwindow.configure(background='grey')
        #size2 = width, height = 600, 600
        #image2 = Image.open(saveImage)
        #got_image2 = image2.resize(size2)
        #photo2 = ImageTk.PhotoImage(got_image2)
        
        self.display = Label(newwindow,image=self.photo)
        self.display.image = self.photo  # keep a reference!
        self.display.image = self.photo
        self.display.place(x=100, y=100)
        imageformat=Label(newwindow,text=str(self.image.format)+" "+str(self.image.mode)+" "+str(self.image.palette)+" "+str(self.image.size))
        imageformat.place(x=100,y=50)
        #Buttion to rotate the Image
        rotate_button=Button(newwindow,text="Rotate",command=self.rotateImage)
        rotate_button.place(x=650,y=100)
        self.userAngle=StringVar()
        w = Spinbox(newwindow,textvariable=self.userAngle, from_=0, to=360)
        w.place(x=700,y=100)
        #Button to blur the image
        blur_button=Button(newwindow,text="Blur",command=self.blurImage)
        blur_button.place(x=650,y=150)
        self.userBlur=StringVar()
        blur_spin=Spinbox(newwindow,textvariable=self.userBlur,from_=0,to=15)
        blur_spin.place(x=700,y=150)
        #Save button
        save_button=Button(newwindow,text="Save Image",command=self.saveImage)
        save_button.place(x=150,y=650)
        #contrast button
        contrast_button=Button(newwindow,text="contrast",command=self.contrastImage)
        contrast_button.place(x=650,y=200)
        #sharpness button
        sharp_button=Button(newwindow,text="Sharpness",command=self.sharpImage)
        sharp_button.place(x=650,y=250)
        #bright button
        bright_button=Button(newwindow,text="Brightness",command=self.brightImage)
        bright_button.place(x=650,y=300)
        #color button
        color_button=Button(newwindow,text="Adjust Color",command=self.colorImage)
        color_button.place(x=650,y=350)
        #crop button
        crop_button=Button(newwindow,text="Crop",command=self.cropImage)
        crop_button.place(x=650,y=400)
        self.first_number=StringVar()
        self.second_number=StringVar()
        first_spin=Spinbox(newwindow,textvariable=self.first_number,from_=0,to=500)
        first_spin.place(x=750,y=400)
        second_spin=Spinbox(newwindow,textvariable=self.second_number,from_=0,to=500)
        second_spin.place(x=900,y=400)

    def saveImage(self):
        pass


    def rotateImage(self):
        self.getAngle=self.userAngle.get()
        self.resizeImage=self.image.resize(self.size)
        self.rotateIm=self.resizeImage.rotate(int(self.getAngle),expand=True)
        self.photo1=ImageTk.PhotoImage(self.rotateIm)
        self.display.configure(image=self.photo1)

    def blurImage(self):
        self.getBlur=self.userBlur.get()
        self.resizeImage_forblurphoto=self.image.resize(self.size)
        self.blurIm=self.resizeImage_forblurphoto.filter(ImageFilter.GaussianBlur(int(self.getBlur)))
        self.blurPhoto=ImageTk.PhotoImage(self.blurIm)
        self.display.configure(image=self.blurPhoto)

    def mergeImages(self):
        pass


    def contrastImage(self):
        pass

    def brightImage(self):
        pass

    def sharpImage(self):
        pass

    def colorImage(self):
        pass

    def cropImage(self):
        pass
 




             
       




root=Tk()
app=MainWindow(root)
root.geometry("1050x850")
root.configure(background="grey")
root.title("Image Editing and Processing")
root.mainloop()

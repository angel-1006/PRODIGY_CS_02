from tkinter import *
from tkinter import filedialog



def encrypt_image():
    file1=filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg')])
    if file1 is not None:
        #print(file1)
        file_name=file1.name
        #print(file_name)
        key=entry1.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            image[index]=values^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()

def decrypt_image():
    file1=filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg')])
    if file1 is not None:
        #print(file1)
        file_name=file1.name
        #print(file_name)
        key=entry2.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            image[index]=values^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()

root=Tk()
root.geometry("500x500")
root.title("ImgCrypt")
root.config(bg="black")

head_frame = Frame(base)
head_frame.pack(pady=10)

head_lable = Label(head_frame, text="Welcome to ImgCrypt", font=("Times New Roman", 30, "bold"), bg="black", fg="white")
head_lable.pack()

subhead_frame = Frame(base)
subhead_frame.pack()

subhead_lable = Label(subhead_frame, text="Author : Kalmux ", font=("Times New Roman", 15, "bold"), bg="black", fg="white")
subhead_lable.pack()

file_frame = Frame(base, bg="black")
file_frame.pack(side=TOP, anchor="nw", pady=5, padx=8)

file_lable = Label(file_frame, text="Image Path:", font=("Times New Roman", 15), bg="black", fg="white")
file_lable.grid(row=1, column=0)

path_value = StringVar()
path_value.set("")
path = Entry(file_frame, textvariable=path_value, font=("Times New Roman", 12), width=50)
path.grid(row=1, column=2)

path_button = Button(file_frame, text="Browse", command=filepath, font=("Times New Roman", 10), padx=10)
path_button.grid(row=1, column=3, padx=5)

key_frame = Frame(base, bg="black")
key_frame.pack(side=TOP, anchor="nw")

space_lable = Label(key_frame, text="", padx=30, bg="black")
space_lable.grid(row=0, column=0)

key_lable = Label(key_frame, text="Key:", font=("Times New Roman", 14), bg="black", fg="white")
key_lable.grid(row=0, column=1)

key_value = IntVar()
key = Entry(key_frame, textvariable=key_value, font=("Times New Roman", 12), width=10)
key.grid(row=0, column=2)

space_lable = Label(key_frame, text="", padx=54, bg="black")
space_lable.grid(row=0, column=3)

encrypt_button = Button(key_frame, text="Encrypt", command=encryption, font=("Times New Roman", 11), width=15)
encrypt_button.grid(row=0, column=4, padx=10)
decrypt_button = Button(key_frame, text="Decrypt", command=decryption, font=("Times New Roman", 11), width=15)
decrypt_button.grid(row=0, column=5, padx=5)

space_frame = Frame(base)
space_frame.pack()

space_lable = Label(space_frame, text="", font=("", 5, "bold"), bg="black", fg="white",)
space_lable.pack()

image_frame = Frame(base, borderwidth=3, relief=SUNKEN, height=200, width=200)
image_frame.pack(side=TOP, anchor="center", expand=False, pady=10)

image_display = Label(image_frame, height=200, width=200, text="No Image Selected")
image_display.pack(expand=True)

image_frame.pack_propagate(False)

foot_frame = Frame(base)
foot_frame.pack()

foot_lable = Label(foot_frame, text="", font=("Times New Roman", 15, "bold"), bg="black", fg="lightgreen")
foot_lable.pack(side=TOP, anchor="center")

b1=Button(root,text="encrypt",command=encrypt_image)
b1.place(x=70,y=10)
b2=Button(root,text="decrypt",command=decrypt_image)
b2.place(x=170,y=10)
entry1=Text(root,height=1,width=10)
entry1.place(x=50,y=50)
entry2=Text(root,height=1,width=10)
entry2.place(x=150,y=50)
base.mainloop()


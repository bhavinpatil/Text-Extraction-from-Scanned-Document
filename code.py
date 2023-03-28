from cgitb import text
from email.mime import image
from http import client, server
import tkinter as tk
from tkinter import filedialog, image_names
from tkinter.filedialog import askopenfile
from urllib import response
from xml.dom.minidom import Document
import boto3
from PIL import Image, ImageTk

my_window = tk.Tk()
my_window.geometry("500x500")
my_window.title("AWS Textract")

l1 = tk.Label(my_window, text="Upload an Image",width=30, font=('times', 18, 'bold'))
l1.pack()

b1 = tk.Button(my_window, text="Upload File", width=15, command=lambda:upload_file())
b1.pack()

def upload_file():
    aws_management_console = boto3.session.Session(profile_name='USER_NAME')   #replace USER_NAME with your IAM user 
    client = aws_management_console.client(service_name = 'textract', region_name = 'REGION')  #replace REGION with your IAM user's region


    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)

    # resizing the uploaded image with respect to window size 
    img_resize = img.resize((350,350))
    img = ImageTk.PhotoImage(img_resize)

    img_to_bytes = get_image_byte(filename)


    l2 = tk.Label(my_window, image = img)
    l2.pack()

    response = client.detect_document_text(Document={'Bytes': img_to_bytes ,})

    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            print(item['Text'])

def get_image_byte(filename):
    with open(filename, 'rb') as imagefile:
        return imagefile.read()


my_window.mainloop()


from chat2_sdk import Chat2Printer
from PIL import Image
printer = Chat2Printer()
im = Image.open('frame.jpg')
printer.print_image(image=im)
from wand.image import Image 

mywidth = 300

with Image(filename = 'z1.jpeg') as img: 
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img.resize(mywidth, hsize) 
    img.save(filename = 'resize.jpeg') 

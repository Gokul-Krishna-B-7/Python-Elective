from PIL import Image

def grey(image):
    for x in range(image.width):
        for y in range(image.height):
            (r,g,b)=image.getpixel((x,y)) #(r.g,b,a) for png images
            r=int(r*0.299)
            g=int(g*0.587)
            b=int(b*0.114)
            lum = r+g+b
            image.putPixel(x,y,(lum,lum,lum))

def main(filename = "img.jpg"):

    image = Image.open(filename)
    
    grey(image)
    
    image.save("grey.png")



if __name__=="__main__":
    main()

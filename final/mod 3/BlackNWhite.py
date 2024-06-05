from PIL import Image

def black(image):
    blackpixel=(0,0,0)
    whitepixel=(255,255,255)
    for x in range(image.width):
        for y in range(image.height):
            (r,g,b)=image.getpixel((x,y)) #(r.g,b,a) for png images
            avg=(r+g+b)//3
            if avg < 128:
                image.putpixel((x,y),blackpixel)
            else:
                image.putpixel((x,y),whitepixel)

def main(filename = "img.jpg"):

    image = Image.open(filename)
    
    black(image)
    
    image.save("black.png")



if __name__=="__main__":
    main()

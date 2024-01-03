from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def cerificate_crate(name):
    img = Image.open('media/myimage/c.jpeg')
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('media/myimage/BusinessSignatureDemo.otf', 100)
    I1.text((487, 650),name, font=myFont, fill =(255, 0, 0))
    img.save(f"media/studentcertificate_image/{name}.png")
    return f"{name}.png"
    # path = os.path.abspath(certificate)

def intoPDF(imagepath,roll):
    i=Image.open(imagepath)  
    h=i.convert("RGB")
    h.save(f"media/studentcertificate_PDF/{roll}.pdf")
    return  f"studentcertificate_PDF/{roll}.pdf"  
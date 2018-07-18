from

def load_img(filename):
    img= Image.open(filename)
    return img

def show_img(im):
    im.show()

def save_img(im, filename):
    im.save(filename, "jpeg")
    show_img(im)

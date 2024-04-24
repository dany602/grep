from PIL import Image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import random 
from image_info import image_info

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# @app.route('/')
# def home():
#     random1 = random.choice(image_info)
#     random2 = random.choice(image_info)
#     random3 = random.choice(image_info)
#     return render_template('home.html',
# id1=random1["id"], title1=random1["title"],
# id2=random2["id"], title2=random2["title"],
# id3=random3["id"], title3=random3["title"]
# )

def open_image(image_info):
    with open(image_info, "rb") as f:
        img_data = f.read()
    return img_data

@app.route('/')
def home():
    random_images = random.sample(image_info, 3) 
    print(random_images)
    image_info = {image: open_image(image) for image in random_images}
    return render_template('index.html', random_images=random_images)
   
@app.route('/detail/<image>')
def detail(image):
    image_info = open_image(image)
    return render_template('detail.html', image_data=image_info)


    
# @app.route('/picture/<id>')
# def image_page(id):
#     for anImage in image_info:
#         if anImage["id"] == id:
#             title = anImage["title"]
# author = Image["flickr_user"]
# image_path = "hw4_images/{image['id']}.jpg"\
# im: Image = Image.open(image_path)
# w = im.width
# h = im.height
# mode = im.mode
# format = im.format
# return render_template('imagePage.html', id=id, title=title, author=author, w=w, h=h, mode=mode, format=format)

# def image_page(id):
#     for images in image_info:
#         if images["id"] == id:
#             title = images["title"]
#             author = images["flickr_user"]
#             image_path = f"hw4_images/{images['id']}.jpg"
#             im = Image.open(image_path)
#             w, h = im.size
#             mode = im.mode
#             img_format = im.format
#             return render_template('index.html', id=id, title=title, author=author, w=w, h=h, mode=mode, format=img_format)
  
if __name__ == "__main__":
    app.run(debug=True)
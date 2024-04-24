from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
import random
from image_info import image_info  # Assuming this contains the list of images

app = Flask(__name__)
bootstrap = Bootstrap5(app)

def open_image(image_info):
    with open(image_info, "rb") as f:
        img_data = f.read()
    return img_data

@app.route('/')
def home():
    random.shuffle(image_info)  # Shuffle the list of images
    selected_images = image_info[:3]  # Select the first three images after shuffling
    return render_template('index.html', images=selected_images)
   
@app.route('/detail/<image>')
def detail(image):
    image_info = open_image(image)
    return render_template('detail.html', image_data=image_info)
 
if __name__ == "__main__":
    app.run(debug=True)

import base64
from io import BytesIO
import os
import random
from flask import Flask, render_template, request, url_for  #fix and add flask components
from flask_bootstrap import Bootstrap5   #fix and add bootstrap component
from random import shuffle
from PIL import Image
from image_info import image_info
from filters import apply_sepia, apply_negative, apply_grayscale, create_thumbnail

"""
    Name: Drake Goldsmith, Jasmin Medrano, Daniel Bonilla Urtis
    Date: 05/13/24
    Course: CST 205: Multimedia Programming
    Description: 
"""

app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    shuffle(image_info)
    random_images = []
    for count in range(3):
        random_images.append(image_info[count])
    return render_template('index.html', random_images=random_images)

@app.route('/picture/<image_id>')
@app.route('/detail/<image_id>')
def detail(image_id):
    for info in image_info:
        if info["id"] == image_id:
            image = info
            break
    image_path = os.path.join(app.root_path, 'static', 'images', f'{image_id}.jpg')
    
    if os.path.exists(image_path):
        with Image.open(image_path) as img:
            width, height = img.size
            mode = img.mode
            image_format = img.format
        return render_template('detail.html', image=image, width=width, height=height, mode=mode, format=image_format)

@app.route('/final')
def final():
    image_id = request.args.get('image_id')
    filter_name = request.args.get('filter')

    for info in image_info:
        if info["id"] == image_id:
            image = info
            break

    image_path = os.path.join(app.root_path, 'static', 'images', f'{image_id}.jpg')
    if os.path.exists(image_path):
        with Image.open(image_path) as img:
            # Apply the selected filter
            if filter_name == 'apply_sepia':
                filtered_image = apply_sepia(img)
            elif filter_name == 'apply_negative':
                filtered_image = apply_negative(img)
            elif filter_name == 'apply_grayscale':
                filtered_image = apply_grayscale(img)
            elif filter_name == 'create_thumbnail':
                filtered_image = create_thumbnail(img)

            filtered_image_path = os.path.join(app.root_path, 'static', 'filtered_images', f'{image_id}_filtered.jpg')
            filtered_image.save(filtered_image_path)
            
    return render_template('final.html', image=image, filtered_image_path=filtered_image_path)


if __name__ == '__main__':
    app.run(debug=True)

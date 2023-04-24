from flask import Flask, request, render_template
from PIL import Image
from doctest import ela


# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']

        # Read the image and save it to disk
        img = Image.open(file)
        img_path = 'uploaded_image.jpg'
        img.save(img_path)

        # Check if the image is fake
        threshold = 83
        is_fake = ela(img_path, scale=10, threshold=threshold)

        # Render the result template with the result message
        return render_template('result.html', is_fake=is_fake)

    # Render the index template with the upload form
    return render_template('index.html')


#if __name__ == '__main__':
    #app.run(debug=True)
    #app.config['DEBUG'] = True
    
@app.route('/test', methods=['POST'])
def test():
    return 'Hello World!'

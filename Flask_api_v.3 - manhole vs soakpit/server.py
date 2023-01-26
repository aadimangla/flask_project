from flask import Flask, request, jsonify
from PIL import Image
from prediction import  predict

app = Flask(__name__)


@app.route("/im_size", methods=["POST"])
def process_image():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)
    output, probs = predict(img)
    print(output, probs)
    output = str(output)
    probs = str(probs)

    return jsonify({'Class': [output], 'Confidence': [probs]})


if __name__ == "__main__":
    app.run()

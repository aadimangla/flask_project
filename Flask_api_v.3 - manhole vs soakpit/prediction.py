# from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np
from skimage import transform


def loadmodel():
    model = load_model('model_soakpitsVmanhole.h5')
    return model


model = loadmodel()


def predict(image: np.ndarray):
    reverse_index = {0: 'ManHole', 1: 'SoakPits'}
    np_image = np.array(image).astype('float32')/255
    np_image = transform.resize(np_image, (350, 350, 3))
    np_image = np.expand_dims(np_image, axis=0)
    prediction = model.predict(np_image)
    print(prediction)
    result = np.argmax(prediction)
    results = reverse_index[result]
    probs = prediction[0][result]
    return results, probs

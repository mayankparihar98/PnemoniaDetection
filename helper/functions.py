from helper.libraries import cv2, np, load_model, Image, ImageOps, img_to_array, preprocess_input

MODEL = './model/MobileNetV2.hdf5'


def input_model():
    print("loading model")

    model = load_model(MODEL)

    return model


def preprocess_image(img):
    size = (224, 224)
    img = Image.open(img)

    if (img is not None):
        img = ImageOps.fit(img, size, Image.ANTIALIAS)
        img = np.asarray(img)
        image1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image1 = cv2.resize(image1, (224, 224))

        image1 = img_to_array(image1)
        image1 = preprocess_input(image1)
        image1 = np.expand_dims(image1, axis=0)

        return image1

    return None


def predict(model, img):
    (normal, pneumonia) = model.predict(img)[0]

    prediction = False if normal > pneumonia else True

    return pneumonia, prediction

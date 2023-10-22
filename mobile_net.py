
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

mobile_net = tf.keras.applications.MobileNetV3Large(
    input_shape=(224, 224, 3),
    alpha=1.0,
    minimalistic=False,
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    classes=1000,
    pooling=None,
    dropout_rate=0.2,
    classifier_activation="softmax",
    include_preprocessing=True,
)

img = image.load_img('nail.jpeg', target_size=(224, 224))
img = image.img_to_array(img)

# 1. Preprocess the image
img = tf.keras.applications.mobilenet_v3.preprocess_input(img)

# 2. Expand dimensions to match the model's expectations
img = tf.expand_dims(img, axis=0)

# 3. Make predictions
predictions = mobile_net.predict(img)

# 4. Decode predictions to get top 5 classes
decoded_predictions = tf.keras.applications.mobilenet_v3.decode_predictions(predictions)

top_5_predictions = decoded_predictions[0][:5]

# Print the top 5 predictions
for i, (imagenet_id, label, score) in enumerate(top_5_predictions):
    print(f"{i + 1}: {label} ({score:.2f})")

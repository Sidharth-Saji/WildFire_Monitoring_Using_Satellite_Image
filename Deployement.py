import tensorflow as tf
import pandas as pd
import os 
from pathlib import Path
# Got the Image Dataframe


def create_df_img(file_path):
    """ Create a DataFrame with the filepath and the labels of the pictures"""

    labels = list(map(lambda x: os.path.split(os.path.split(x)[0])[1], file_path))
    file__path = pd.Series(file_path, name='Filepath').astype(str)
    labels = pd.Series(labels, name='Label')
    df = pd.concat([file__path, labels], axis=1)
    return df


test_dir = Path('Forest2.jpg')
filepath = [test_dir]

df_test = create_df_img(filepath)
print(df_test.head())

test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(dtype='float32', rescale=1./255.)
test_generator = test_datagen.flow_from_dataframe(df_test,
                                                  x_col='Filepath',
                                                  y_col='Label',
                                                  shuffle=False,
                                                  batch_size=1,
                                                  target_size=(350, 350),
                                                  class_mode='categorical')


model = tf.keras.models.load_model('WildFireDetector.h5')
prediction = model.predict(test_generator)
print(pd)


if prediction[0][1] > 0.90:
    print(prediction[0][1], 'WildFire Occurring TAke Preventive Measures ')
elif prediction[0][1] < 0.03:
    print(prediction[0][1], 'Hmm Looks Like the place is safe')

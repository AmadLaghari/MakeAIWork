import numpy as np
import pandas as pd
# from keras.backend.tensorflow_backend import set_session
#from keras.models import Sequential
#from keras import applications
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


dataframe = pd.read_csv('C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/sonar.samples', header = None, sep = ' ')

#dataframe.to_csv('C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/sonar.samples', header = ["dist1","dist2","dist3","angle"], index=False)

#print (np.array(dataframe))

#print (df.shape)


numpyarray = np.array(dataframe)
arr_distances = []
arr_steering = []
for x in numpyarray:
    distancesSonar = float(x[0].split(',')[0]), float(x[0].split(',')[1]), float(x[0].split(',')[2])
    steeringSonar =  float(x[0].split(',')[3])
    #print(train_single)
    data_np = np.asarray(distancesSonar, np.float32)
    s = tf.convert_to_tensor(data_np, np.float32)
    arr_distances.append(distancesSonar)
    arr_steering.append(steeringSonar)


val_arr_distances = np.array(arr_distances[0:299])
val_arr_steering = np.array(arr_steering[0:299])

model = tf.keras.Sequential([

    tf.keras.Input(shape=(3,)), 
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(3, )]
    ) 


model.compile(
optimizer='adam',
loss='mean_squared_error',
metrics=[
    'accuracy',
    
])
 #tf.keras.losses.MeanSquaredError() 'mean_squared_error'
model.fit(arr_distances, arr_steering, epochs=1000)



probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])

prediction = probability_model.predict(val_arr_distances)

print(prediction)


# De overfit voorkomen (functie evaluate) Validation om de data te controleren dat het overeenkomt met de resultaat (testset)
# test_loss, test_acc = model.evaluate(val_arr_distances,  test_arr_steering, verbose=2)
# print('\nTest accuracy:', test_acc, '\nTest loss:', test_loss)



# De overfit voorkomen (functie evaluate) Validation om de data te controleren dat het overeenkomt met de resultaat (testset)
# Stuurhoeken normaliseren en linken aan werkelijke stuurhoeken
# Implementatie met hardcoded
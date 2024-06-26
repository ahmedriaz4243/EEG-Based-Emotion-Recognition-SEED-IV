# -*- coding: utf-8 -*-
"""BCI_TL_Within_Subject_EEG-ITNet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16ZppsWfIp6Q6IUKkReLMDS0xPvWgy1Ad
"""

pip install mne

pip install tensorflow_addons

"""# Data Loading (SEED-IV): Load the extracted and transformed data

"""

import scipy.io
import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import warnings
import scipy.signal as signal
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# Ignore warnings
warnings.filterwarnings('ignore')

# Mount Google Drive
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

GOOGLE_DRIVE_PATH_AFTER_MYDRIVE = os.path.join('CE807/BCITL/Data/eeg_raw_data')
GOOGLE_DRIVE_PATH = os.path.join('gdrive', 'MyDrive', GOOGLE_DRIVE_PATH_AFTER_MYDRIVE)
print('List session files: ', os.listdir(GOOGLE_DRIVE_PATH))

import sys
sys.path.append('/content/gdrive/My Drive/CE807/BCITL/Code')
import tensorflow as tf
import tl_helper

from sklearn import metrics
from keras.callbacks import EarlyStopping, ModelCheckpoint
from tl_helper import preprocess_eeg, split_eeg
from tl_helper import process_file, divide_data
from tl_helper import get_session_labels ,get_categorical_labels
from tl_helper import get_participant_files
from tl_helper import get_session_number
from tl_helper import  process_eeg_chunks_for_EEGNET
from tl_helper import EEGNet,  EEGNet_FirstLayerOnly
print ("Import tl_helper sucessfully")

from sklearn import metrics
from keras.callbacks import EarlyStopping, ModelCheckpoint

def data_preprocessing_splitting(participant_files, num_participants, participant_num, n_chunks):
    session1_label, session2_label, session3_label = get_session_labels()
    print("  *** **** ")
    print("Participant Data:", participant_num)

    for session_num in range(1, 4):  # Loop through session 1, session 2, and session 3
        # Find the appropriate session label based on the current session number

        # Get the files for the current participant
        files = participant_files[participant_num]
        # Sort the files based on the session number and get session number from path
        sorted_files = sorted(files, key=get_session_number)

        file_path = sorted_files[session_num - 1]  # Adjust the index since sessions are 1-indexed

        if session_num == 1:
            print("Session 1 file_path session1_label: ", file_path)
            eeg_chunks_list_train_S1, label_list_S1 = process_file(file_path, session1_label, n_chunks)

        elif session_num == 2:
            print("Session 2 file_path session2_label: ", file_path)
            eeg_chunks_list_tune_S2, label_list_tune_S2, eeg_chunks_list_train_S2, label_list_train_S2 = divide_data(file_path, session2_label, n_chunks)

        elif session_num == 3:
            print("Session 3 file_path session3_label: ", file_path)
            eeg_chunks_list_tune_S3, label_list_tune_S3, eeg_chunks_list_train_S3, label_list_train_S3 = divide_data(file_path, session3_label, n_chunks)

            # For Participant i - Session 1

            print(" *** ** Participant Data Summary ** *** : ",  participant_num)

            print("Participant - Session 1")
            print("No of Trails (Train) ", len(eeg_chunks_list_train_S1))
            print("Shape of each eeg_chunks ", eeg_chunks_list_train_S1[0].shape)
            print("----------------------")

            # For Participant i - Session 2
            print("Participant - Session 2")
            print("No of Trails (Train)", len(eeg_chunks_list_train_S2))
            print("Shape of eeg_chunks", eeg_chunks_list_train_S2[0].shape)
            print("No of Trails (Tune)", len(eeg_chunks_list_tune_S2))
            print("Shape of eeg_chunks",  eeg_chunks_list_tune_S2[0].shape)
            print("----------------------")

            # For Participant i - Session 3
            print("Participant - Session 3")
            print("No of Trails (Train)",len(eeg_chunks_list_train_S3))
            print("Shape of eeg_chunks", eeg_chunks_list_train_S3[0].shape)
            print("No of Trails (Tune)", len(eeg_chunks_list_tune_S3))
            print("Shape of eeg_chunks", eeg_chunks_list_tune_S3[0].shape)
            print("----------------------")

            print("-----------process_eeg_chunks_for_Modeling-----------")

            ChunkData_session1 = process_eeg_chunks_for_EEGNET(eeg_chunks_list_train_S1)
            ChunkData_session2_train = process_eeg_chunks_for_EEGNET(eeg_chunks_list_train_S2)
            ChunkData_session2_tune = process_eeg_chunks_for_EEGNET(eeg_chunks_list_tune_S2)
            ChunkData_session3_train = process_eeg_chunks_for_EEGNET(eeg_chunks_list_train_S3)
            ChunkData_session3_tune = process_eeg_chunks_for_EEGNET(eeg_chunks_list_tune_S3)

            categorical_labels, categorical_labels_2_tune, categorical_labels_2_train, categorical_labels_3_tune, categorical_labels_3_train = get_categorical_labels(label_list_S1, label_list_tune_S2, label_list_train_S2, label_list_tune_S3, label_list_train_S3)
            print("ChunkData_session1_train : ", ChunkData_session1.shape)
            print("ChunkData_session2_train : ", ChunkData_session2_train.shape)
            print("ChunkData_session2_tune : ", ChunkData_session2_tune.shape)
            print("ChunkData_session3_train : ", ChunkData_session3_train.shape)
            print("ChunkData_session3_tune : ", ChunkData_session3_tune.shape)



            print("-----------data_preprocessing_splitting_done-----------")
    # Return the required variables
    return (
        ChunkData_session1,
        ChunkData_session2_train,
        ChunkData_session2_tune,
        ChunkData_session3_train,
        ChunkData_session3_tune,
        categorical_labels,
        categorical_labels_2_tune,
        categorical_labels_2_train,
        categorical_labels_3_tune,
        categorical_labels_3_train
    )

"""@Pipeline"""

participant_files = get_participant_files(GOOGLE_DRIVE_PATH)
print ("participant_files : ", participant_files)
num_participants = 15
participant_num = 15
n_chunks = 700

# Call the function and store the returned values
(
    ChunkData_session1,
    ChunkData_session2_train,
    ChunkData_session2_tune,
    ChunkData_session3_train,
    ChunkData_session3_tune,
    categorical_labels,
    categorical_labels_2_tune,
    categorical_labels_2_train,
    categorical_labels_3_tune,
    categorical_labels_3_train
) = data_preprocessing_splitting(participant_files, num_participants, participant_num, n_chunks)

def modeling_EEGNet_ITNet(ChunkData_session1, ChunkData_session2_train, ChunkData_session2_tune,
                       ChunkData_session3_train, ChunkData_session3_tune, categorical_labels,
                       categorical_labels_2_train, categorical_labels_2_tune, categorical_labels_3_train,
                       categorical_labels_3_tune, nb_classes=4, Chans=62, Samples=500, participant_num=1):


    print("categorical_labels.shape ", categorical_labels.shape)
    print("categorical_labels_2_train:", categorical_labels_2_train.shape)
    print("Categorical_labels_2_tune:", categorical_labels_2_tune.shape)
    print("categorical_labels_3_train:", categorical_labels_3_train.shape)
    print("categorical_labels_3_tune:", categorical_labels_3_tune.shape)

    print("ChunkData_session1_train : ", ChunkData_session1.shape)
    print("ChunkData_session2_train : ", ChunkData_session2_train.shape)
    print("ChunkData_session2_tune : ", ChunkData_session2_tune.shape)
    print("ChunkData_session3_train : ", ChunkData_session3_train.shape)
    print("ChunkData_session3_tune : ", ChunkData_session3_tune.shape)

    # Modeling
    nb_classes = 4
    Chans = 62
    Samples = 700  # timepoints

     # Modeling
    model1 = EEG_ITNet(Chans, Samples)  # Create model1 using EEG_ITNet architecture
    #model2 = EEG_ITNet_FirstTwoLayers(Chans, Samples)
    model2 = create_frozen_EEG_ITNet(Chans, Samples)

    # Compile both models
    model1.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    early_stopping = EarlyStopping(monitor='val_loss', patience=600, mode='min', verbose=1, restore_best_weights=True)

    model_filename = f"trained_model1_participant_{participant_num}.h5"
    model_checkpoint = ModelCheckpoint(model_filename, monitor='val_loss', save_best_only=True, mode='min')

    # Combine the callbacks in a list
    callbacks = [early_stopping, model_checkpoint]

    print("model1.summary()", model1.summary())


    # First Session Training (Using model1)
    print("model1 training ******** ")
    fitted1 = model1.fit(ChunkData_session1, categorical_labels, epochs=300, validation_split=0.1, callbacks=callbacks,
               batch_size=128)


    # Transfer Learning for Second and Third Session (Using model2)
    print("model2 training ******** ")

    # Load pretrained weights from model1 into model2
    model2.set_weights(model1.get_weights())

    # For Third Session     # For Second Session
    categorical_labels_train = np.append(categorical_labels_2_train, categorical_labels_3_train, axis=0)
    print("categorical_labels_train shape: ", categorical_labels_train.shape)
    ChunkData_train = np.append(ChunkData_session2_train, ChunkData_session3_train, axis=0)
    print("ChunkData_train shape: ", ChunkData_train.shape)


    print("model2.summary()", model2.summary())
    fitted2 = model2.fit(ChunkData_train, categorical_labels_train, epochs=300, validation_split=0.1, callbacks=callbacks,
               batch_size=128)
    plot_training_history(fitted2)


    # Define the EarlyStopping callback and mode save
    early_stopping = EarlyStopping(monitor='val_loss', patience=100, mode='min', restore_best_weights=True)
    # Define the ModelCheckpoint callback to save the best model during training
    model_filename = f"trained_model2_participant_{participant_num}.h5"
    model_checkpoint = ModelCheckpoint(model_filename, monitor='val_loss', save_best_only=True, mode='min')

    print("   **********   ")

    print("   ***** Data Arrangement*****   ")

    categorical_labels_tune = np.append(categorical_labels_2_tune, categorical_labels_3_tune, axis=0)
    print("categorical_labels_tune shape: ", categorical_labels_tune.shape)
    ChunkData_tune = np.append(ChunkData_session2_tune, ChunkData_session3_tune, axis=0)
    print("ChunkData_tune shape: ", ChunkData_tune.shape)

    predicted = model2.predict(x=ChunkData_tune)

    # Convert true labels to multiclass format
    true_labels_multiclass = np.argmax(categorical_labels_tune, axis=1)
    predicted_labels_multiclass = np.argmax(predicted, axis=1)

    # Calculate accuracy
    accuracy = metrics.accuracy_score(true_labels_multiclass, predicted_labels_multiclass)
    print("Accuracy:", accuracy)

    # Calculate F1-score
    f1_score = metrics.f1_score(true_labels_multiclass, predicted_labels_multiclass, average='weighted')
    print("F1-score:", f1_score)

    # Calculate precision, recall, and F1-score for each class
    classification_report = metrics.classification_report(true_labels_multiclass, predicted_labels_multiclass)
    print("Classification Report:", classification_report)

Chans = 62
Samples = 700
participant_num = 15
modeling_EEGNet_ITNet(ChunkData_session1, ChunkData_session2_train, ChunkData_session2_train,
                                                                    ChunkData_session3_train, ChunkData_session3_tune,
                                                                    categorical_labels, categorical_labels_2_train,
                                                                    categorical_labels_2_train, categorical_labels_3_train,
                                                                    categorical_labels_3_tune, Chans, Samples, participant_num)

"""### EEGNET // https://arxiv.org/abs/1611.08024
### EEGITNET  //https://arxiv.org/abs/2204.06947
"""


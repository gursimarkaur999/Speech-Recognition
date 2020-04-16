# MFCC is what we need to extract from datasets for speech recognition
# tells timbre of audio

import librosa
import os
import json

dataset_path = "dataset"
json_path = " data.json"
# librosa uses something called sample rate which is standard 22050 #1 sec worth of sound
total_samples= 22050

# extract mfcc from all audio files and store in json file and then our deep learning model will use this info for training
# Mfcc structure has 3 specific arguements 
def prep_dataset(dataset_path, json_path, ):
    
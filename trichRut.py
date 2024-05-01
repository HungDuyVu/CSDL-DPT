import librosa
import numpy as np

# Đường dẫn đến file âm thanh
audio_file = 'D:\Work\CSDL - ĐPT\ss2.mp3'

# Đọc file âm thanh
y, sr = librosa.load(audio_file)

# Trích rút đặc trưng MFCC
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# Trích rút đặc trưng chroma
chroma = librosa.feature.chroma_stft(y=y, sr=sr)

# Trích rút đặc trưng spectral contrast
spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)

# Trích rút đặc trưng zero-crossing rate
zero_crossing_rate = librosa.feature.zero_crossing_rate(y)

# Trích rút đặc trưng RMS
rms = librosa.feature.rms(y=y)

# Trích rút đặc trưng spectral centroid và bandwidth
spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)

# In ra kích thước của các ma trận đặc trưng
print("MFCC shape:", mfccs.shape)
print("Chroma shape:", chroma.shape)
print("Spectral Contrast shape:", spectral_contrast.shape)
print("Zero-Crossing Rate shape:", zero_crossing_rate.shape)
print("RMS shape:", rms.shape)
print("Spectral Centroid shape:", spectral_centroid.shape)
print("Spectral Bandwidth shape:", spectral_bandwidth.shape)

import json

# Kích thước của các ma trận đặc trưng
mfcc_shape = (13, 3505)
chroma_shape = (12, 3505)
spectral_contrast_shape = (7, 3505)
zero_crossing_rate_shape = (1, 3505)
rms_shape = (1, 3505)
spectral_centroid_shape = (1, 3505)
spectral_bandwidth_shape = (1, 3505)

# Tạo một từ điển chứa thông tin về các đặc trưng
feature_data = {
    'MFCC': mfcc_shape,
    'Chroma': chroma_shape,
    'Spectral Contrast': spectral_contrast_shape,
    'Zero-Crossing Rate': zero_crossing_rate_shape,
    'RMS': rms_shape,
    'Spectral Centroid': spectral_centroid_shape,
    'Spectral Bandwidth': spectral_bandwidth_shape
}

# Xuất dữ liệu dưới dạng JSON
with open('feature_data.json', 'w') as json_file:
    json.dump(feature_data, json_file, indent=4)


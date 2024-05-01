import json
import numpy as np
import librosa
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

def extract_features(file_path):
    y, sr = librosa.load(file_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
    rms = librosa.feature.rms(y=y)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    
    return {'MFCC': mfccs.tolist(), 'Chroma': chroma.tolist(), 'Spectral Contrast': spectral_contrast.tolist(), 
            'Zero-Crossing Rate': zero_crossing_rate.tolist(), 'RMS': rms.tolist(), 
            'Spectral Centroid': spectral_centroid.tolist(), 'Spectral Bandwidth': spectral_bandwidth.tolist()}

def compare_audio(features_1, features_2):
    # Sử dụng DTW để so sánh hai file âm thanh
    distances = {}
    for key, value in features_1.items():
        distance, _ = fastdtw(np.array(value).T, np.array(features_2[key]).T, dist=euclidean)
        distances[key] = distance
    return distances

def compute_similarity(target_features, features_data):
    # Tính toán độ tương đồng giữa file cần so sánh và các file trong dữ liệu
    similarities = {}
    for file, features in features_data.items():
        similarity = compare_audio(target_features, features)
        similarities[file] = similarity
    
    return similarities

# Đọc dữ liệu đặc trưng từ file JSON
def read_feature_data_from_json(json_file):
    with open(json_file, 'r') as f:
        feature_data = json.load(f)
    return feature_data

# Đường dẫn đến file JSON chứa dữ liệu đặc trưng
json_file = 'D:\\Work\\CSDL - ĐPT\\audio_features_shape.json'
# Đường dẫn đến file audio cần so sánh
target_audio_file = 'D:\\Work\\CSDL - ĐPT\\Test.mp3'

# Trích xuất đặc trưng của file audio cần so sánh
target_features = extract_features(target_audio_file)

# Đọc dữ liệu đặc trưng từ file JSON
features_data = read_feature_data_from_json(json_file)

# Tính toán độ tương đồng giữa file cần so sánh và các file trong dữ liệu
similarities = compute_similarity(target_features, features_data)

# Lấy ra 3 file có độ tương đồng cao nhất
top_3_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:3]

# In kết quả
for file, similarity in top_3_similarities:
    print("File:", file)
    print("Similarity:", similarity)

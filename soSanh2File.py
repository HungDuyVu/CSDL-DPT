import librosa
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def extract_features(file_path):
    # Đọc file âm thanh và lấy mẫu âm thanh
    signal, sample_rate = librosa.load(file_path, sr=None)
    
    # Trích xuất các đặc trưng âm thanh
    mfcc_features = librosa.feature.mfcc(y=signal, sr=sample_rate)
    chroma_features = librosa.feature.chroma_stft(y=signal, sr=sample_rate)
    spectral_contrast_features = librosa.feature.spectral_contrast(y=signal, sr=sample_rate)
    zero_crossing_rate_features = librosa.feature.zero_crossing_rate(y=signal)
    rms_features = librosa.feature.rms(y=signal)
    spectral_centroid_features = librosa.feature.spectral_centroid(y=signal, sr=sample_rate)
    spectral_bandwidth_features = librosa.feature.spectral_bandwidth(y=signal, sr=sample_rate)
    
    return mfcc_features, chroma_features, spectral_contrast_features, zero_crossing_rate_features, rms_features, spectral_centroid_features, spectral_bandwidth_features

def compare_audio(file_path_1, file_path_2):
    # Trích xuất đặc trưng cho hai file âm thanh
    features_1 = extract_features(file_path_1)
    features_2 = extract_features(file_path_2)
    
    # Sử dụng DTW để so sánh hai file âm thanh
    distances = []
    for i in range(len(features_1)):
        distance, path = fastdtw(features_1[i].T, features_2[i].T, dist=euclidean)
        distances.append(distance)
    
    return distances

def compute_similarity(file_path_1, file_path_2):
    # So sánh hai file âm thanh
    distances = compare_audio(file_path_1, file_path_2)
    
    # Tính tổng của tất cả các giá trị distance
    total_distance = sum(distances)
    
    # Tìm giá trị lớn nhất trong mảng distances
    max_distance = max(distances)
    
    # Tính toán độ tương đồng
    similarity = 1 - (max_distance / total_distance) if total_distance != 0 else 1.0
    
    return similarity * 100

# Đường dẫn đến hai file âm thanh cần so sánh
file_path_1 = r"D:\Work\CSDL - ĐPT\ss2.mp3"
file_path_2 = r"D:\Work\CSDL - ĐPT\ss2.mp3"

# So sánh hai file âm thanh
distances = compare_audio(file_path_1, file_path_2)
print("Distances between features:")
print("MFCC:", distances[0])
print("Chroma:", distances[1])
print("Spectral Contrast:", distances[2])
print("Zero-Crossing Rate:", distances[3])
print("RMS:", distances[4])
print("Spectral Centroid:", distances[5])
print("Spectral Bandwidth:", distances[6])

# Tính toán độ tương đồng giữa hai file âm thanh
similarity = compute_similarity(file_path_1, file_path_2)
print("Similarity between audio files:", similarity, "%")

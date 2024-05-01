import os
import json
import librosa

# Đường dẫn đến thư mục chứa các file âm thanh
directory_path = r'D:\Work\CSDL - ĐPT\audio_files'

# Danh sách các đặc trưng cần trích rút
feature_names = ['MFCC', 'Chroma', 'Spectral Contrast', 'Zero-Crossing Rate', 'RMS', 'Spectral Centroid', 'Spectral Bandwidth']

# Hàm trích rút đặc trưng từ một file âm thanh
def extract_features(audio_file):
    y, sr = librosa.load(audio_file)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
    rms = librosa.feature.rms(y=y)
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    
    return {'MFCC': mfccs.shape, 'Chroma': chroma.shape, 'Spectral Contrast': spectral_contrast.shape, 
            'Zero-Crossing Rate': zero_crossing_rate.shape, 'RMS': rms.shape, 
            'Spectral Centroid': spectral_centroid.shape, 'Spectral Bandwidth': spectral_bandwidth.shape}

# Hàm trích rút đặc trưng từ một thư mục chứa nhiều file âm thanh
def extract_features_from_directory(directory_path):
    all_features = {}
    # Duyệt qua từng file trong thư mục
    for filename in os.listdir(directory_path):
        if filename.endswith('.mp3'):
            file_path = os.path.join(directory_path, filename)
            features = extract_features(file_path)
            all_features[filename] = features
    return all_features

# Trích rút đặc trưng từ thư mục chứa nhiều file âm thanh
audio_features = extract_features_from_directory(directory_path)

# Ghi dữ liệu vào tệp JSON
output_file = 'audio_features_shape.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(audio_features, f, ensure_ascii=False, indent=4)


# print("Đã lưu kích thước của các đặc trưng vào tệp:", output_file)

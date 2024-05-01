import os

# Get the current directory path
current_directory = os.getcwd()

def remove_special_characters(filename):
    # Loại bỏ các ký tự đặc biệt
    special_chars = "!@#$%^&*()[]{};:,./<>?\\|`~-=_+0123456789"
    for char in special_chars:
        filename = filename.replace(char, "")
    return filename

def rename_files(folder_path):
    # Lặp qua tất cả các tệp trong thư mục
    for index, filename in enumerate(os.listdir(folder_path), start=1):
        # Tạo đường dẫn đầy đủ cho từng tệp
        old_filepath = os.path.join(folder_path, filename)
        
        # Kiểm tra xem tệp có phải là tệp không?
        if os.path.isfile(old_filepath):
            # Loại bỏ ký tự dấu cách
            new_filename = remove_special_characters(filename).replace(" ", "")
            # Tạo số thứ tự cho tên tệp mới
            new_filename = str(index) + "_" + new_filename + ".mp3"
            
            # Đường dẫn mới cho tệp
            new_filepath = os.path.join(folder_path, new_filename)
            
            # Đổi tên tệp
            os.rename(old_filepath, new_filepath)

# Đường dẫn thư mục chứa các tệp
folder_path = f'{current_directory}/audio'

# Gọi hàm để đổi tên các tệp
rename_files(folder_path)

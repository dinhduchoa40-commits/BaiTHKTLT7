def copy_file(source, destination):
    try:
        with open(source, 'r', encoding='utf-8') as src:
            content = src.read()
        
        with open(destination, 'w', encoding='utf-8') as dest:
            dest.write(content)
        
        print(f"Đã sao chép thành công từ '{source}' sang '{destination}'")
        
        # Kiểm tra kết quả
        with open(destination, 'r', encoding='utf-8') as check:
            print(f"File đích có {len(check.readlines())} dòng")
            
    except FileNotFoundError:
        print(f"Không tìm thấy file nguồn: {source}")
    except PermissionError:
        print("Không có quyền truy cập file")
    except Exception as e:
        print(f"Lỗi: {e}")

# Sử dụng
copy_file('test.txt', 'copy_test.txt')

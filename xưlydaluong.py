import threading
import time

# Hàm thực thi của mỗi luồng
def print_numbers(thread_name, delay):
    """In ra các số từ 1 đến 5 với độ trễ giữa các lần in"""
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{thread_name}: {count}")

# Tạo các luồng
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 1))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 2))

# Khởi chạy các luồng
thread1.start()
thread2.start()

# Đợi tất cả các luồng hoàn thành
thread1.join()
thread2.join()

print("Tất cả các luồng đã hoàn thành!")
#Định nghĩa hàm thực thi: Hàm print_numbers sẽ được thực thi bởi mỗi luồng, in ra các số từ 1 đến 5 với độ trễ giữa các lần in.

#Tạo luồng:

#threading.Thread() tạo một đối tượng luồng mới

#target chỉ định hàm sẽ được thực thi

#args là các tham số truyền vào hàm target

#Khởi chạy luồng:

#start() bắt đầu thực thi luồng

#Đợi luồng hoàn thành:

#join() đảm bảo chương trình chính sẽ đợi đến khi luồng hoàn thành
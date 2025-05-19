import threading
import random
import math
import time

class Lab1(threading.Thread):
    def __init__(self, _id, A, bat_dau, ket_thuc):
        super().__init__()
        self.id = _id
        self.A = A
        self.starts = bat_dau
        self.end = ket_thuc
        self.dem_scp = 0
    
    def run(self):
        for i in range(self.starts, self.end):
            if self.scp(self.A[i]):
                self.dem_scp += 1
                print(f"T-{self.id}: {self.A[i]} - {time.strftime('%H:%M:%S', time.localtime())}")
        
        with khoa:
            global tong_scp
            tong_scp += self.dem_scp

    def scp(self, n):
        cbh = math.isqrt(n)
        return cbh * cbh == n

if __name__ == "__main__":
    while True:
        try:
            N = int(input("Nhập N: "))
            if N <= 10:
                print("N > 100!!!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập số nguyên!")

    while True:
        try:
            k = int(input("Nhập k: "))
            if k <= 1:
                print("k > 1!!!")
                continue
            break
        except ValueError:
            print("Vui lòng nhập số nguyên!")
    A = [random.randint(1, 100) for _ in range(N - 1)]
    A.append(4)
    tong_scp = 0
    khoa = threading.Lock()

    print(f"\nMảng A được tạo với {N} phần tử ngẫu nhiên:")
    print(A[:N])  

    spt = N // k
    threads = []

    for i in range(k):
        starts = i * spt # Vị trí bắt đầu = chỉ số luồng * số phần tử mỗi luồng
        end = (i + 1) * spt if i != k - 1 else N # Luồng cuối nhận phần dư
        t = Lab1(i, A, starts, end)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print(f"\nTổng số số chính phương trong mảng: {tong_scp}")
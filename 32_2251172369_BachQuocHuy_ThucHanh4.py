from xmlrpc.server import SimpleXMLRPCServer

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def X(N):  # Đổi tên hàm thành X
    try:
        N = int(N)
        primes = [x for x in range(2, N + 1) if is_prime(x)]
        print(primes)
        return primes
    except:
        return "Dữ liệu không hợp lệ"

# Tạo server và đăng ký hàm X
server = SimpleXMLRPCServer(("0.0.0.0", 8001), allow_none=True)
server.register_function(X, "X1")

print("RPC Server đang chạy trên cổng...")
server.serve_forever()

def extract_flag(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    start = 2000
    flag_bytes = []
    for i in range(50):
        c = 0
        for j in range(8):
            byte = data[start + i * 8 + j]
            c |= (byte & 1) << j
        flag_bytes.append((c + 5) & 0xFF)  # vì mã gốc dùng (char - 5)

    return bytes(flag_bytes).decode()

if __name__ == "__main__":
    flag = extract_flag("encoded.bmp")
    print("[✅] Recovered flag:", flag)

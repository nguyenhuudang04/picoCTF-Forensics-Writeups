                                                       
def extract_flag_from_mystery(filename):
    with open(filename, "rb") as f:
        data = f.read()

    embedded = data[-26:]

    flag = bytearray()

    flag.extend(embedded[0:4])

    flag.append(embedded[4])
    flag.append(embedded[5])

    for i in range(6, 15):
        flag.append((embedded[i] - 5) % 256)

    flag.append((embedded[15] + 3) % 256)

    flag.extend(embedded[16:26])

    print("Flag:", flag.decode(errors="replace"))


extract_flag_from_mystery("mystery.png")


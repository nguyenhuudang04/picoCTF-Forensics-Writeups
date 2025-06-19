with open("encoded.bmp", "rb") as f:
    f.seek(0x2d3)
    result = ""
    
    for k in range(50):
        binary = ""
        for j in range(8):
            byte = f.read(1)
            if not byte:
                break
            lsb = ord(byte) & 1
            binary = str(lsb) + binary  
        
        result += chr(int(binary, 2))
        f.read(1) 
    print("Flag:", result)

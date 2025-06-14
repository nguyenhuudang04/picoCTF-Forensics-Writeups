def reverse_each_4byte_block(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = bytearray(f.read())
    result = bytearray()
    for i in range(0, len(data), 4):
        block = data[i:i+4]
        result.extend(block[::-1])  
    with open(output_file, 'wb') as f:
        f.write(result)
    print(f"save file : {output_file}")
reverse_each_4byte_block("challengefile", "reversed_blocks_challengefile")

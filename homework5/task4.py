# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

def encode(input_line):
    encoded_str = ""
    tmp_char = None
    tmp_char_count = 0
    for char in input_line:
        if char != tmp_char:
            if tmp_char_count > 0:
                encoded_str += str(tmp_char_count) + tmp_char
            tmp_char = char
            tmp_char_count = 0
        tmp_char_count += 1
    encoded_str += str(tmp_char_count) + tmp_char
    return encoded_str


def decode(input_line: str):
    decoded_string = ""
    tmp_num = 0
    for char in input_line:
        if char.isdigit():
            if tmp_num > 0:
                tmp_num = tmp_num * 10 + int(char)
            else:
                tmp_num = int(char)
        else:
            decoded_string += char * tmp_num
            tmp_num = 0
    return decoded_string


# encode
with open("encode_input.txt", "r") as file:
    original = file.read().rstrip()
encoded = encode(original)
print(f"{original} => {encoded}")
with open("encode_output.txt", "w") as file:
    file.write(encoded)


# decode
with open("decode_input.txt", "r") as file:
    original = file.read().rstrip()
decoded = decode(original)
print(f"{original} => {decoded}")
with open("decode_output.txt", "w") as file:
    file.write(decoded)

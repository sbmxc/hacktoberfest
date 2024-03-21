# LANGUAGE: Python
# ENV: Python 3.8.6
# AUTHOR: Mohd Baqer Haider
# GITHUB: https://github.com/haider000

def BinaryToDecimal(binary):   
    return int(binary, 2)

msg = "010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001"

str_data =''

for i in range(0, len(msg), 8): 
    temp_data = msg[i:i + 8] 
    decimal_data = BinaryToDecimal(temp_data) 
    str_data = str_data + chr(decimal_data) 

print(str_data)
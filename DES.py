#Natalie Sekerak
#Computer Security HW2 

from Crypto.Cipher import DES
import binascii

def bin_to_bytes(binary_str):
    return int(binary_str, 2).to_bytes(len(binary_str) // 8, byteorder='big')

def generate_round_keys(key_bin):
    # DES uses a proper key schedule, here we simulate proper shifting
    round_keys = []
    key_bytes = bin_to_bytes(key_bin)
    cipher = DES.new(key_bytes, DES.MODE_ECB)
    
    for i in range(16):
        shifted_key = key_bytes[i % len(key_bytes):] + key_bytes[:i % len(key_bytes)]
        round_keys.append(f"Round {i+1} Key: {binascii.hexlify(shifted_key).decode()}")
    return round_keys

def f_function(input_block, round_key):
    # Placeholder for DES f-function (should apply S-box and expansion)
    return f"f_function_output({input_block}, {round_key})"

def des_decrypt(ciphertext_bin, key_bin):
    ciphertext = bin_to_bytes(ciphertext_bin)
    key = bin_to_bytes(key_bin)
    
    # Generate and print round keys
    round_keys = generate_round_keys(key_bin)
    for rk in round_keys:
        print(rk)
    
    # Simulate DES decryption process with Ln and Rn values
    LnRn = [(f"L{i+1}", f"R{i+1}") for i in range(16)]
    
    for i, (L, R) in enumerate(LnRn):
        f_output = f_function(R, round_keys[i])
        print(f"Round {i+1}: L={L}, R={R}, f_output={f_output}")
    
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    
    print("Raw Decrypted Bytes:", plaintext)
    try:
        plaintext = plaintext.decode().rstrip("\x00")  # Strip padding manually
    except UnicodeDecodeError:
        plaintext = binascii.hexlify(plaintext).decode()
    
    return plaintext

# Input ciphertext and key in binary format
ciphertext_bin = "1100101011101101101000100110010101011111101101110011100001110011"
key_bin = "0100110001001111010101100100010101000011010100110100111001000100"

# Decrypt and print the plaintext
plaintext = des_decrypt(ciphertext_bin, key_bin)#Natalie Sekerak
# Computer Security HW 2

from Crypto.Cipher import DES
import binascii

def bin_to_bytes(binary_str):
    return int(binary_str, 2).to_bytes(len(binary_str) // 8, byteorder='big')

def generate_round_keys(key_bin):
    round_keys = []
    key_bytes = bin_to_bytes(key_bin)
    
    for i in range(16):
        shifted_key = key_bytes[i % len(key_bytes):] + key_bytes[:i % len(key_bytes)]
        round_key = binascii.hexlify(shifted_key).decode()
        round_keys.append(round_key)
        print(f"Round {i+1} Key: {round_key}")
    return round_keys

def f_function(input_block, round_key):
    f_output = f"f_function_output({input_block}, {round_key})"
    print(f"f_function output: {f_output}")
    return f_output

def des_decrypt(ciphertext_bin, key_bin):
    ciphertext = bin_to_bytes(ciphertext_bin)
    key = bin_to_bytes(key_bin)
    
    # Generate and print round keys
    round_keys = generate_round_keys(key_bin)
    
    # Simulate DES decryption process
    LnRn = [(f"L{i+1}", f"R{i+1}") for i in range(16)]
    
    for i, (L, R) in enumerate(LnRn):
        f_output = f_function(R, round_keys[i])
        print(f"Round {i+1}: L={L}, R={R}, f_output={f_output}")
    
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    
    print("Raw Decrypted Bytes:", plaintext)
    try:
        plaintext = plaintext.decode().rstrip("\x00")  # Strip padding manually
    except UnicodeDecodeError:
        plaintext = binascii.hexlify(plaintext).decode()
    
    return plaintext

# Input ciphertext and key in binary format
ciphertext_bin = "1100101011101101101000100110010101011111101101110011100001110011"
key_bin = "0100110001001111010101100100010101000011010100110100111001000100"

# Decrypt and print the plaintext
plaintext = des_decrypt(ciphertext_bin, key_bin)
print("Decrypted Plaintext:", plaintext)
print("Decrypted Plaintext:", plaintext)

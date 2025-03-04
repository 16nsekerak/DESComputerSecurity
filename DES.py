#Natalie Sekerak
#HW 2

import binascii

############### DES TABLES ###############
IP = [
    58, 50, 42, 34, 26, 18, 10,  2,
    60, 52, 44, 36, 28, 20, 12,  4,
    62, 54, 46, 38, 30, 22, 14,  6,
    64, 56, 48, 40, 32, 24, 16,  8,
    57, 49, 41, 33, 25, 17,  9,  1,
    59, 51, 43, 35, 27, 19, 11,  3,
    61, 53, 45, 37, 29, 21, 13,  5,
    63, 55, 47, 39, 31, 23, 15,  7
]

FP = [
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
]

PC1 = [
    57, 49, 41, 33, 25, 17,  9,
     1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12,  4
]

PC2 = [
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

E_table = [
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
]

P = [
    16,  7, 20, 21,
    29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25
]

S_BOXES = [
    # S1
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],
    # S2
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],
    # S3
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ],
    # S4
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],
    # S5
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],
    # S6
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ],
    # S7
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],
    # S8
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
]

############### bitwise operations helper functions ###############
def permute(in_bits, table):
    return [in_bits[pos - 1] for pos in table]

def left_rotate(bits, shift):
    return bits[shift:] + bits[:shift]

# Helps with the list handling
def xor_bits(a, b):
    return [x ^ y for x, y in zip(a, b)]

def binstr_to_bytes(bin_str):
    # Convert binary string -> integer
    val = int(bin_str, 2)
    # Format as hex with enough digits
    #    (every 4 bits = 1 hex digit, so length//4 hex digits)
    hex_len = len(bin_str) // 4
    hex_str = f"{val:0{hex_len}x}"  
    # Convert hex -> bytes
    return binascii.unhexlify(hex_str)

def bytes_to_binstr(b):
    hex_str = binascii.hexlify(b).decode('ascii')
    # hex -> int -> binary string
    val = int(hex_str, 16)
    bin_len = len(b) * 8  # total bits
    return f"{val:0{bin_len}b}"


def bytes_to_bitlist(b):
    bit_list = []
    for byte in b:
        for i in range(8):
            bit_list.append((byte >> (7 - i)) & 1)
    return bit_list

def bitlist_to_bytes(bit_list):
    out = bytearray()
    for i in range(0, len(bit_list), 8):
        val = 0
        for j in range(8):
            val = (val << 1) | bit_list[i + j]
        out.append(val)
    return bytes(out)


############### Important functions ###############
def sbox_substitution(bits48):
    output = []
    for i in range(8):
        block6 = bits48[i*6:(i+1)*6]
        row = (block6[0] << 1) | block6[5]
        col = (block6[1] << 3) | (block6[2] << 2) | (block6[3] << 1) | block6[4]
        val = S_BOXES[i][row][col]
        # 4 bits of 'val'
        for s in range(4):
            output.append((val >> (3 - s)) & 1)
    return output

def f_function(r32, subkey48):
    # Expand R from 32->48, xor, sbox and permute
    expanded = permute(r32, E_table)
    xored = xor_bits(expanded, subkey48)
    s_out = sbox_substitution(xored)
    return permute(s_out, P)

def generate_subkeys(key64bits):
    key56 = permute(key64bits, PC1)
    C = key56[:28]
    D = key56[28:]

    subkeys = []
    for round_i in range(16):
        shift_amount = SHIFT_SCHEDULE[round_i]
        C = left_rotate(C, shift_amount)
        D = left_rotate(D, shift_amount)
        # PC-2 => 48 bits
        CD = C + D
        K_i = permute(CD, PC2)
        print(f"Key{15-round_i:2} = {''.join(map(str, K_i))}")
        subkeys.append(K_i)
    return subkeys[::-1] # return the reversed key order to decrypt


def des_decrypt_block(cipher64bits, subkeys):
    # Initial Permutation
    perm_out = permute(cipher64bits, IP)
    L = perm_out[:32]
    R = perm_out[32:]

    # 16 rounds
    for i in range(16):
        round_key = subkeys[i] 
        f_out = f_function(R, round_key)

        key_str = "".join(str(x) for x in round_key)
        f_str =  "".join(str(x) for x in f_out)
        print(f"Round {i+1}")
        print(f"  f(R_{i}, K_{i}) = {f_str}")

        # Feistel
        new_L = R
        new_R = xor_bits(L, f_out)
        L, R = new_L, new_R

        print(f"  L_{i+1} = {''.join(map(str, L))}")
        print(f"  R_{i+1} = {''.join(map(str, R))}")

    preoutput = R + L
    plain64bits = permute(preoutput, FP)
    return plain64bits

def main():

    # Provided info
    key_str = "LOVECSND"
    key_bytes = key_str.encode("ascii")  # 8 bytes
    ciphertext_binstr = "1100101011101101101000100110010101011111101101110011100001110011"

    ciphertext_block = binstr_to_bytes(ciphertext_binstr)

    key_bits_64 = bytes_to_bitlist(key_bytes)
    print("16 Keys:")
    subkeys_enc = generate_subkeys(key_bits_64)  # K1..K16 (in reverse order)
   
    
    ct_bits_64 = bytes_to_bitlist(ciphertext_block)
    print("\nDecode\n")
    plaintext_bits_64 = des_decrypt_block(ct_bits_64, subkeys_enc)
    print(f"\nPlaintext (binary) = {''.join(map(str, plaintext_bits_64))}")

    # Convert the resulting 64 bits into ASCII
    plaintext_block = bitlist_to_bytes(plaintext_bits_64)
    plaintext_str = plaintext_block.decode('ascii', errors='replace')
    print(f"Message = {plaintext_str}")

if __name__ == "__main__":
    main()
sbox = (
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
        )
sbox_inv = (
        0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
        0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
        0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
        0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
        0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
        0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
        0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
        0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
        0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
        0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
        0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
        0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
        0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
        0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
        0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
        )
rcon = (
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)

def form_matrix(bits):
    matrix = [[0 for x in range(4)] for y in range(4)]
    for y in range(0,4):
        for x in range(0,4):
            print(bits[2*x+8*y:(2*x+8*y)+2])
            if bits[2*x+8*y:(2*x+8*y)+2] == '':
                print("yeet")
            matrix[x][y] = int(bits[2*x+8*y:(2*x+8*y)+2],16)
    return matrix

def matrix_to_word(matrix):
    word = ""
    for col in range(0,4):
        for row in range(0,4):
            if matrix[row][col] < 16:
                word += "0" + hex(matrix[row][col])[2:]
            else:
                word += hex(matrix[row][col])[2:]
    return word


def shift_matrix(matrix):
    for x in range(0,4):
        arr = [0]*4
        for y in range(0,4):
            arr[y] = matrix[x][(y+x)%4]
        for z in range(0,4):
            matrix[x][z] = arr[z]
    return matrix


def inv_shift_matrix(matrix):
    for x in range(0,4):
        arr = [0]*4
        for y in range(0,4):
            arr[y] = matrix[x][(y-x)%4]
        for z in range(0,4):
            matrix[x][z] = arr[z]
    return matrix


def sub_bytes(matrix):
    for x in range(0,4):
        for y in range(0,4):
            index = matrix[x][y]
            matrix[x][y] = sbox[index]
    return matrix


def mix_columns(matrix):
    val_matrix = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    new_matrix = [[0 for x in range(4)] for y in range(4)]
    for col in range(0,4):
        for row in range(0,4):
            arr = [0] * 4
            for x in range(0,4):
                # Case of three
                if val_matrix[row][x] == 3:
                    arr[x] = (matrix[x][col] * 2) ^ matrix[x][col]
                else:
                    arr[x] = (matrix[x][col] * val_matrix[row][x])
            temp = arr[0] ^ arr[1] ^ arr[2] ^ arr[3]
            if temp > 255:
                temp ^= 283
            new_matrix[row][col] = temp
    return new_matrix

def key_expansion(key,mode):
    exp_key = key
    itr = 0
    # 128 bit
    if mode == 1:
        while len(exp_key) < 352:
            for i in range(0,4):
                temp1 = exp_key[-8:]
                if i == 0:
                    temp1 = key_expansion_core(temp1, itr)
                    itr += 1
                temp2 = exp_key[-32:]
                temp2 = temp2[:8]
                text = hex(int(temp1, 16) ^ int(temp2, 16))[2:]
                while len(text) < 8:
                    text = "0" + text
                exp_key += text
    # 192 bit
    elif mode == 2:
        while len(exp_key) < 420:
            for i in range(0,6):
                temp1 = exp_key[-8:]
                if i == 0:
                    temp1 = key_expansion_core(temp1,itr)
                    itr += 1
                temp2 = exp_key[-48:]
                temp2 = temp2[:8]
                text = hex(int(temp1, 16) ^ int(temp2, 16))[2:]
                while len(text) < 8:
                    text = "0" + text
                exp_key += text
    # 240
    elif mode == 3:
        while len(exp_key) < 480:
            for i in range(0,8):
                temp1 = exp_key[-8:]
                if i == 0:
                    temp1 = key_expansion_core(temp1,itr)
                    itr += 1
                # S-box
                if i == 4:
                    bits = [temp1[0:2], temp1[2:4], temp1[4:6], temp1[6:8]]
                    for x in range(0, 4):
                        index = int(bits[x],16)
                        bits[x] = hex(sbox[index])[2:]
                        # zero pad as needed
                        if int(bits[x], 16) < 16:
                            bits[x] = "0" + bits[x]
                    temp1 = bits[0]+bits[1]+bits[2]+bits[3]
                temp2 = exp_key[-64:]
                temp2 = temp2[:8]
                text = hex(int(temp1, 16) ^ int(temp2, 16))[2:]
                while len(text) < 8:
                    text = "0" + text
                exp_key += text
    return exp_key




def key_expansion_core(bits,itr):
    # shift left
    bits = [bits[2:4],bits[4:6],bits[6:8],bits[0:2]]
    # sub bytes
    for x in range(0,4):
        temp = bits[x]
        index = int(temp,16)
        #index = int(temp[0], 16) * int(temp[1]+'0', 16)
        bits[x] = sbox[index]
    # round constant
    bits[0] ^= rcon[itr]
    '''
    if itr > 7:
        bits[0] ^= (2 ** itr) ^ 283
        print(hex(bits[0])[2:])
    else:
        bits[0] ^= 2 ** itr
    '''
    # zero pad as needed
    for x in range(0,4):
        if bits[x] < 16:
            bits[x] = "0" + hex(bits[x])[2:]
        else:
            bits[x] = hex(bits[x])[2:]
    #print(bits)
    return bits[0]+bits[1]+bits[2]+bits[3]


# Main function
word = "1526154061b689e0f00a5c2ff1ec19e4"
key = "30190dcc14585301f5bfc5b666c84775"
#key = "2B7E151628AED2A6ABF7158809CF4F3C"
mode = 1
rounds = 0
if mode == 1:
    rounds = 9
elif mode == 2:
    rounds = 11
else:
    rounds == 13
key = key_expansion(key,mode)
for itr in range(0,rounds):
    word = hex(int(word,16) ^ int(key[16*itr:16*(itr+1)],16))[2:]
    print(word)
    mat = form_matrix(word)
    mat = sub_bytes(mat)
    mat = shift_matrix(mat)
    mat = mix_columns(mat)
    word = matrix_to_word(mat)
# last round
word = hex(int(word,16) ^ int(key[16*rounds:16*(rounds+1)],16))[2:]
mat = form_matrix(word)
mat = sub_bytes(mat)
mat = shift_matrix(mat)
word = matrix_to_word(mat)
word = hex(int(word,16) ^ int(key[16*rounds:16*(rounds+1)],16))[2:]
print(word)

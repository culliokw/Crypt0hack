state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

# function definition brought over from solution file to the Symmetric Ciphers Structures of AES challenge
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return [x for y in matrix for x in y]

# We iterate through each column of every row and take the XOR value between the current state and the key to obtain the keyed permutation
def add_round_key(s, k):
    return [[s[y][x]^k[y][x] for x in range(0,4)] for y in range(0,4)]


finalMatrix = add_round_key(state,round_key)

# Perform the necessary type conversion and Voila we have our flag
print([chr (x) for x in matrix2bytes(finalMatrix)])




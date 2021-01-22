import math

# Robust Hash Size : 256 bit hex
PHASH_SIZE = 32
HIGH_FREQ_FACTOR = 16

# no of approx images for training
NO_OF_TRAINED_IMAGES = 5

# Robust hashing Parameters
NUMBER_OF_ROBUST_BLOCKS = 16
ROBUST_BLOCK_SIZE = 16

# Cryptographic hash parameters: 128 bit cyrpto hash value
CRYPTOGRAPHIC_HASH_BLOCKS = 8
CRYPTOGRAPHIC_BLOCK_SIZE = 16

# Training and testing folder data mapping

folder_mapping_dict = {'compressed': "E:\\M.Tech 1 - sem\\Algorithm\\Project\\Dataset\\compressed",
                       'training': "E:\\M.Tech 1 - sem\\Algorithm\\Project\\Dataset\\training\\",
                       'scaled': "E:\\M.Tech 1 - sem\\Algorithm\\Project\\Dataset\\scaled\\",
                       'rotated': "E:\\M.Tech 1 - sem\\Algorithm\\Project\\Dataset\\rotated\\",
                       'random': "E:\\M.Tech 1 - sem\\Algorithm\\Project\\Dataset\\random\\"}

SIMILARITY_THRESHOLD=0.825

def find_bloom_filter_size():
    temp_size = NO_OF_TRAINED_IMAGES * 1 * NUMBER_OF_ROBUST_BLOCKS * CRYPTOGRAPHIC_HASH_BLOCKS
    temp_size = temp_size / 0.70
    bf_size = find_next_prime(int(temp_size))
    return bf_size


# Function that returns True if n
# is prime else returns False
def isPrime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def find_next_prime(temp_size):
    # Base case
    if temp_size <= 1:
        return 2

    prime = temp_size
    found = False

    # Loop continuously until isPrime returns
    # True for a number greater than n
    while not found:
        prime = prime + 1
        if isPrime(prime):
            found = True

    return prime


# Bloom Filter Size
BF_SIZE = int(find_bloom_filter_size())
print("Bloom Filter Size:"+str(BF_SIZE))
BLOOM_FILTER = [0] * int(BF_SIZE)

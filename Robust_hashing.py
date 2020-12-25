import imagehash
import numpy
from PIL import Image
import distance
from Constants import *


# use 24 bit hash size
# 144 bits hash --> divide into 8 groups of 18 bits each
# 18 + block_number(4) bits


def chunkstring(string, length):
    return (string[0 + i:length + i] for i in range(0, len(string), length))


def compute_robust_hash(image_name):
    hash_val = imagehash.phash(Image.open(image_name), PHASH_SIZE,
                               HIGH_FREQ_FACTOR)
    print(hash_val)
    robust_hash_blocks = []
    robust_hash_blocks = list(chunkstring(str(hash_val), ROBUST_BLOCK_SIZE))
    # print(robust_hash_blocks)

    # -- Append Block numbers to each block
    for i in range(0, NUMBER_OF_ROBUST_BLOCKS):
        robust_hash_blocks[i] = robust_hash_blocks[i] + '{:04b}'.format(i);
    return robust_hash_blocks


compute_robust_hash("E:\\M.Tech 1 - sem\\Algorithm\\Project\\Dataset\\compressed\\du94v9qtxs54257kt306.jpg")

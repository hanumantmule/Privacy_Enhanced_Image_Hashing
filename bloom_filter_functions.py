BLOOM_FILTER = [0] * 64


def compute_bloom_filter_index(hex1):
    # print(int(hex1, 16))
    # convert them to integers, add them, and modulo the answer by 2^64 to get it back into a 16 char hex
    return (int(hex1, 16)) % (2 ** 6)

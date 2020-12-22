import Robust_hashing
from Read_Images import load_images_from_folder
from cryptographic_hashing import *
from Constants import *
import bloom_filter_functions


def get_folder_name(test_type):
    return folder_mapping_dict[test_type]


def test_image(test_type):
    robust_hash_blocks = []
    image_list = []
    folder_name = get_folder_name(test_type)
    image_list = load_images_from_folder(folder_name)
    result = " "
    for image in image_list:
        print(image)
        robust_hash_blocks = Robust_hashing.compute_robust_hash(image)
        print(robust_hash_blocks)

        zero_count = 0
        one_count = 0
        for hash_block in robust_hash_blocks:
            crpytographic_hash = compute_cryptographic_hash(hash_block)
            print(crpytographic_hash)
            print("\n-----------\n")
            crpytographic_hash_blocks = list(Robust_hashing.chunkstring(str(crpytographic_hash), CRYPTOGRAPHIC_BLOCK_SIZE))
            print(crpytographic_hash_blocks)
            for crypto_block in crpytographic_hash_blocks:
                block_index = bloom_filter_functions.compute_bloom_filter_index(crypto_block)
                if bloom_filter_functions.BLOOM_FILTER[block_index] == 1:
                    one_count = one_count + 1
                else:
                    zero_count = zero_count + 1
            print("\n")

        print(one_count)
        print(zero_count)
        result = result + " One Count: "
        result = result + str(one_count)
        result = result + ", Zero Count: "
        result = result + str(zero_count)
        result = result + " ; "
    return result


test_image('compressed')
import Robust_hashing
from Read_Images import load_images_from_folder
from cryptographic_hashing import *
from Constants import *
import bloom_filter_functions


def main_algo_flow():
    robust_hash_blocks = []
    image_list = []
    folder_path = folder_mapping_dict['training']
    print('Selected Folder Path:'+str(folder_path))
    image_list = load_images_from_folder(folder_path)
    print('List of images present in the folder:')
    for img in image_list:
        print(img)
    for image in image_list:
        print('Selected Image:'+str(image))
        robust_hash_blocks = Robust_hashing.compute_robust_hash(image)
        count = 0
        block_counter=1
        for hash_block in robust_hash_blocks:
            print('Running for Robust Block #:'+str(block_counter))
            block_counter = block_counter+1
            crpytographic_hash = compute_cryptographic_hash(hash_block)
            print('Cryptographic Hash of Image for robust block : '+ str(crpytographic_hash))
            crpytographic_hash_blocks = list(
                Robust_hashing.chunkstring(str(crpytographic_hash), CRYPTOGRAPHIC_BLOCK_SIZE))
            # print(crpytographic_hash_blocks)
            for crypto_block in crpytographic_hash_blocks:
                block_index = bloom_filter_functions.compute_bloom_filter_index(crypto_block)
                bloom_filter_functions.BLOOM_FILTER[block_index] = 1
                count = count + 1
        print("\n-----------\n")
    print('Bloom Filter Content:')
    print(bloom_filter_functions.BLOOM_FILTER)

    return bloom_filter_functions.BLOOM_FILTER
    # test_image()


# main_algo_flow()

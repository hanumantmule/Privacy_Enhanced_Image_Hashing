import Robust_hashing
from Read_Images import load_images_from_folder
from Result_Graphs import plot_graph
from cryptographic_hashing import *
from Constants import *
import bloom_filter_functions
import os


def get_folder_name(test_type):
    return folder_mapping_dict[test_type]


def test_image(test_type):
    folder_name = get_folder_name(test_type)
    image_list = load_images_from_folder(folder_name)
    result = " "
    x_val_list = []
    y_val_list = []
    recall_x_list=range(1,len(image_list)+1)
    recall_y_list=[]
    for image in image_list:
        print(image)
        img_ratio = ''.join(filter(lambda i: i.isdigit(), os.path.basename(image)))

        robust_hash_blocks = Robust_hashing.compute_robust_hash(image)
        print(robust_hash_blocks)

        zero_count = 0
        one_count = 0
        for hash_block in robust_hash_blocks:
            crpytographic_hash = compute_cryptographic_hash(hash_block)
            print(crpytographic_hash)
            print("\n-----------\n")
            crpytographic_hash_blocks = list(
                Robust_hashing.chunkstring(str(crpytographic_hash), CRYPTOGRAPHIC_BLOCK_SIZE))
            print(crpytographic_hash_blocks)
            for crypto_block in crpytographic_hash_blocks:
                block_index = bloom_filter_functions.compute_bloom_filter_index(crypto_block)
                if bloom_filter_functions.BLOOM_FILTER[block_index] == 1:
                    one_count = one_count + 1
                else:
                    zero_count = zero_count + 1
            print("\n")

        image_name = os.path.basename(image)
        similarity = 1 - (zero_count * 0.5 / (NUMBER_OF_ROBUST_BLOCKS * CRYPTOGRAPHIC_HASH_BLOCKS));
        if img_ratio is not '':
            x_val_list.append(img_ratio[1:])
            y_val_list.append(similarity)
        recall_y_list.append(similarity)
        status = "Reject"
        if similarity >= SIMILARITY_THRESHOLD:
            status = "Accept"
        result = result + str(similarity) + "," + image_name + "," + str(one_count) + "," + str(
            zero_count) + "," + status + ";"
    # print(x_val_list,y_val_list)
    plot_graph(x_val_list, y_val_list, test_type+' Ratio', 'Similarity Score', test_type+' Graph','graph_'+test_type+'.png')
    # plot_graph(recall_x_list, recall_y_list, test_type+' Ratio', 'Similarity Score', test_type+' Recall Graph','recall_graph_'+test_type+'.png')

    return result[:-1]

# test_image('compressed')

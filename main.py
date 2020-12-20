
import Robust_hashing
from cryptographic_hashing import *
from Constants import *
import bloom_filter_functions
from test_evaluations import test_image

robust_hash_blocks = []
robust_hash_blocks= Robust_hashing.compute_robust_hash('E:\\M.Tech 1 - sem\\Algorithm\\Project\\Dataset\\Red\\10.jpg')
print(robust_hash_blocks)

for hash_block in robust_hash_blocks:
    crpytographic_hash=compute_cryptographic_hash(hash_block)
    print(crpytographic_hash)
    print("\n-----------\n")
    crpytographic_hash_blocks = list(Robust_hashing.chunkstring(str(crpytographic_hash), CRYPTOGRAPHIC_BLOCK_SIZE))
    print(crpytographic_hash_blocks)
    for crypto_block in crpytographic_hash_blocks:
        block_index=bloom_filter_functions.compute_bloom_filter_index(crypto_block)
        bloom_filter_functions.BLOOM_FILTER[block_index]=1
    print("\n")

print(bloom_filter_functions.BLOOM_FILTER)
test_image()
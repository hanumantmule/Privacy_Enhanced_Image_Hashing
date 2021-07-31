# Privacy-Enhanced Robust Image Hashing with Bloom Filters

Consider the situation of the forensic investigation. Whether suspect posseses a illegal images like child pornography etc. Manul analysis of images is impractical and time consuming, also there is no privacy preservation. Common approach is to use cryptographic hash functions, Match the cryptographic hashes of the master images with the suspects computer images. But slight alteration to the image produces entirely different hash value ( Avalanche effect). So we cannot detect the slightly altered images. Another approach is Robust hashing -- Robust hash provides similar hash for similar images. But problem here is leakage of structural information of image. You can predict the structure of the image using robust hash.    combining cryptographic and robust hashes, we can combine the advantages of both robustness and protection against data leakage.  Use bloom filter to store the image hash values. The reasons to use a bloom filter instead of a regular database is that bloom filters are both space and time efficient. 

Bloom Filter Size : (No of Images *number of partitions* number of blocks per partition * number of indices per block)/log2

##Steps to store an Image
1. A robust hash is obtained using pHash – 256 bit hex generated.
2. Each robust hash is divided into 16 blocks each of 16 bits each.
3. 4 bits block number is added to each block.
4. Each block is cryptographically hashed using Blake_2b technique from hashlib library- 128 bit hex generated.
5. Each Cryptographic hash is split into 8 indices of size 16 bits each.
6. Each Index is mapped into the interval of the Bloom Filter bit array.
7. Each indexed bit position in the bit array is set.

##Steps to check an Image
1. Each indexed bit position in the bit array is checked.
2. If all bit positions belonging to the same cryptographic hash (and the same block) are set, the block is identified. If one bit is not set the block is not contained.
3. Determined the similarity score for the robust hash, taking the results of all tested blocks into account.



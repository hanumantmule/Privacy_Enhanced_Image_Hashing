# Privacy-Enhanced Robust Image Hashing with Bloom Filters

## Steps to store an Image

1. A robust hash is obtained from pHash of size 144 hex bits.
2. At least one partition is used to divide the robust hash into multiple blocks.
   Robust hash is divided into 8 blocks of size 18 bits each. Added 4 bits block number. 
3. Each 22 bits block is cryptographically hashed using Blake2b and 128 bit hex is generated.
4. Each Cryptographic hash is split into 2 indices.
5. Each Index is mapped into the interval of the Bloom Filter bit array.
6. Each indexed bit position in the bit array is set.



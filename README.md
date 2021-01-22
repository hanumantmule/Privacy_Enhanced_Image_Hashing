# Privacy-Enhanced Robust Image Hashing with Bloom Filters

## Steps to store an Image

1. A robust hash is obtained from pHash of size 256 hex bits.
2. At least one partition is used to divide the robust hash into multiple blocks.
   Robust hash is divided into 16 blocks of size 16 bits each. Added 4 bits block number to the 16 bits. 
3. Each 20 bits block is cryptographically hashed using Blake2b and 128 bit hex hash is generated.
4. Each Cryptographic hash is split into 8 indices each of size 16 bits.
5. Each Index is mapped into the interval of the Bloom Filter bit array.
6. Each indexed bit position in the bit array is set.



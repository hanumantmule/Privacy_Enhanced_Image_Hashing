import hashlib


def compute_cryptographic_hash(hash_value):
    blake2_hash = hashlib.blake2b(hash_value.encode('utf-8')).hexdigest()
    return blake2_hash

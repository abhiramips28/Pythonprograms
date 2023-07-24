def hash_key( key, l):

    return key % l

l = 7

print(f'The hash value for 3 is {hash_key(3,l)}')

print(f'The hash value for 2 is {hash_key(2,l)}')

print(f'The hash value for 9 is {hash_key(9,l)}')

print(f'The hash value for 11 is {hash_key(11,l)}')

print(f'The hash value for 7 is {hash_key(7,l)}')
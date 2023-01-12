import math
import random

# bitwise xor of two bit strings
def xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a))


# generate all n bit strings
def gen_n_bit_strings(n: int) -> set:
    res = set()
    for i in range(0, int(math.pow(2,n))):
        res.add(bin(i)[2:].zfill(n))
    return res

# generate a random 2 -> 1 mapping from the set of n bit string using secret bit string s to work with simons algorithm 
# f(x) = f(x ^ s) 
def gen_random_mapping(n: int, s: str) -> dict:
    domain = gen_n_bit_strings(n)
    codmain = gen_n_bit_strings(n)
    mapping = {}
    for x in domain:
        random_num = random.randint(0, len(codmain) - 1)
        mapping[x] = list(codmain)[random_num]
        mapping[xor(x, s)] = mapping[x]
        codmain.remove(mapping[x])
    return mapping


# generate table view of mapping
def gen_table_view(mapping: dict) -> str:
    res = ""
    for x in mapping:
        res += x + " -> " + mapping[x] + "\n"
    return res


# testing
if __name__ == "__main__":
    mapping = gen_random_mapping(4, input("Enter secret string length 4: "))
    print(gen_table_view(mapping))

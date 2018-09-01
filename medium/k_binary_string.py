import sys

def main(args):
    """
    Given k, and a binary string, determine if this contains all permutations of length k.
    For example, 11001 contains all possible binary sequences with k=2 (00,01,10,11)

    Return: T/F
    """
    string_to_check = args[0]
    k = int(args[1])

    string_combinations = []

    for i in range(len(string_to_check) - (k-1)):
        string_combinations.append(string_to_check[i:i+k])

    print(list_contains(string_combinations, k))

def list_contains(string_list, k):
    for i in range(int(pow(2, k))):
        if bin(i)[2:].zfill(k) not in string_list:
            return False

    return True

if __name__ == "__main__":
   main(sys.argv[1:])

# python3


def max_pairwise_product(numbers):
    a = max(numbers)
    b = numbers
    b.remove(max(numbers))
    d = max(b)
    return a*d




if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))




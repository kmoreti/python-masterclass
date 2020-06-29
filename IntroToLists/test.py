max_value = 1000000000


def calc(n: int):
    if n == 1:
        return 0
    result = 1
    if n > 1:
        for f in range(2, n):
            result += f
            if result > max_value:
                break
    return result


def Solution(A):
    m = dict()
    for i in A:
        if i not in m:
            m[i] = 1
        else:
            m[i] = m[i] + 1
    total = 0
    for v in m:
        total += calc(m[v])
        if total > max_value:
            return max_value
    return total


def main():

    A = [3, 5, 6, 3, 3, 5]
    print(Solution(A))
    A = [-3, 5, 6, -3, -3, 5, -3, 4, 6, 6, -3, 4]
    print(Solution(A))
    A = [3, 5, 6, 3, 3, 5, 3, 4, 6, 6, 3, 4, 3, 5, 6, 3, 3, 53, 5, 6, 3, 3, 53, 5, 6, 3, 3, 5, 1, 1, 1, 1, 1]
    print(Solution(A))


if __name__ == '__main__':
    main()

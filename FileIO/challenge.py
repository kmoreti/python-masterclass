with open("sample2.txt", 'w') as sample_file:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{0:>2} times {1} is {2}".format(j, i, i * j), file=sample_file)
        print("-" * 20, file=sample_file)


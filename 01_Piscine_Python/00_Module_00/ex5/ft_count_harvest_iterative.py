def ft_count_harvest_iterative():
    total = int(input("Days until harvest: "))
    total += 1
    for day in range(1, total):
        print("Day", day)
    print("Harvest time!")
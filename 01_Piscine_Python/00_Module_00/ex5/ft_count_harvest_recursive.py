def ft_count_harvest_recursive():
    def count_days(days):
        def count_days_aux(days, end):
            if days > end:
                count_days_aux(days - 1, end)
                print("Day", days)
        count_days_aux(days, 0)
        print("Harvest time!")
    days = int(input("Days until harvest: "))
    count_days(days)
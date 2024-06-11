class QuickSort:

    def swap_values(self, list_to_sort: list, i: int, j: int) -> None:
        list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]


    def quick_sort(self, list_to_sort: list, start = 0, end = None) -> list:

        list_length = len(list_to_sort[start: end])

        if list_length == 0:
            return

        elif list_length == 1:
            return list_to_sort

        # The case were the list is of length two or more
        else:
            if end == None:
                pivot_position = -1
            else:
                pivot_position = end - 1 # To get the new pivot position

            pivot_value = list_to_sort[pivot_position]
            j = start
            print(pivot_position, start + list_length, end)
            for i in range(start, start + list_length):

                if list_to_sort[i] < pivot_value:
                    if list_to_sort[i] < list_to_sort[j]:
                        # i is ahead of j because their values are different
                        # both j and j are less then pivot
                        self.swap_values(list_to_sort, i, j)

                        j += 1 # can be increased as value of j is less than pivotq
                    elif list_to_sort[i] > list_to_sort[j]:
                        # # both j and j are less then pivot
                        # i is ahead of j because their values are different
                         j += 1 # can be increased as value of j is less than pivotq

                elif list_to_sort[i] > pivot_value:
                    if list_to_sort[j] < pivot_value:
                        j += 1

                elif list_to_sort[i] == pivot_value:
                    # i has reached the end of list
                    # There can be to possibilities:

                    # 1. The pivot is greater than the value at j. Pivot should not move.
                    if list_to_sort[i] > list_to_sort[j]:
                        self.quick_sort(list_to_sort, start, i)

                    # 2. The pivot is lower than value at j. Pivot should move.
                    # Hence, passing first and second part back to quick_sort()
                    if list_to_sort[i] < list_to_sort[j]:

                        self.swap_values(list_to_sort, i, j)
                        self.quick_sort(list_to_sort, start, j)
                        self.quick_sort(list_to_sort, j+1, end)

            return list_to_sort




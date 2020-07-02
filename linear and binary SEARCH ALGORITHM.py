# linear search


def search(list_to_be_searched, n):
    for i in range(1, len(list_to_be_searched)):
        if list_to_be_searched[i] == n:
            print('FOUND')
            break
    else:
        print('VALUE NOT FOUND')


list_to_be_searched = [1, 5, 2, 4, 6, 7, 3, 9, 8]
n = 10

search(list_to_be_searched, n)


# binary search

def search(list_to_be_searched, n):

    l = 0
    u = len(list_to_be_searched)-1
    while l <= u:
        mid = (l + u) // 2
        if list_to_be_searched[mid] == n:
            print('FOUND')
            break

        elif list_to_be_searched[mid] < n:
            l = mid+1

        else:
            u = mid-1
    else:
        return print('VALUE NOT FOUND')


list_to_be_searched = [1, 2, 4, 6, 7, 9, 14, 15, 18, 25, 32, 28, 42]
n = 402

search(list_to_be_searched, n)

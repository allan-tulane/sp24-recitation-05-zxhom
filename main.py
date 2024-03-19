import random, time
import tabulate

#random.seed(1)
# for repeatability


def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return (L)
    else:
        m = L.index(min(L))
        print('selecting minimum %s' % L[m])
        L[0], L[m] = L[m], L[0]
        print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])
    #return [L[0]] + selection_sort(L[1:])


def qsort(a, pivot_fn):
    ### Fixed Pivot Implementation
    #p = a[0]

    ### Random Pivot Implementation
    #p = random.choice(a)

    # Base case 0 or 1??
    if len(a) <= 1:
        return a
    else:
        p = pivot_fn(a)  # integer element
        l = list(filter(lambda x: x < p, a))  # unsorted left list
        m = list(filter(lambda x: x == p, a))  # pivot list
        r = list(filter(lambda x: x > p, a))  # unsorted right list
        return qsort(l, pivot_fn) + m + qsort(r, pivot_fn)


def first_pivot(a):  # added
    return a[0]


def random_pivot(a):  # added
    return random.choice(a)


def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###


def compare_sort(sizes=[50, 100, 150, 200, 250, 300, 350, 400, 450, 500]):
    #sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison

    qsort_fixed_pivot = lambda a: qsort(a, first_pivot)  # changed
    qsort_random_pivot = lambda a: qsort(a, random_pivot)  # changed
    tim_sort = lambda a: sorted(a)  # compare timsort last
    selection_sort = lambda a: ssort(a)

    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        #random.shuffle(mylist)
        # need to shuffle before sorting to eliminate recursion error; compiler issue
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            # time_search(selection_sort, mylist),
            time_search(tim_sort, mylist)
        ])
    return result
    ###


def print_results(results):
    """ change as needed for comparisons """
    print(
        tabulate.tabulate(results,
                          headers=[
                              'n', 'qsort-fixed-pivot', 'qsort-random-pivot',
                              'tim-sort'
                          ],
                          floatfmt=".3f",
                          tablefmt="github"))


def test_print():
    print_results(compare_sort())


random.seed()
test_print()

#
#
# print(qsort(testlist, random_pivot))

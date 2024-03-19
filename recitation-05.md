# CMPS 2200 Recitation 5

In this recitation, we'll look at randomness in computation.

**To make grading easier, please place all written solutions directly in `answers.md`, rather than scanning in handwritten work or editing this file.**

All coding portions should go in `main.py` as usual.


## Determinism versus Randomization in Quicksort

In lecture we saw that adding a random choice of pivot reduced the
probability of worst-case behavior for any given input in
selection. Let's look at how pivot choices affect Quicksort. For this
question, refer to the code in `main.py` 

**1a)**

Complete the implementations of `qsort` and `compare_sort` stubs. Feel
free to take from code given in the lectures to  help you perform list
partitioning. Note that the pivot choice function is input to `qsort`,
so you will have to curry `qsort` to test different methods of
choosing pivots. Implement variants of `qsort` that correspond to
selecting the first element of the input list as the pivot, and to
selecting a random pivot.
.  
.  
.  
.  


**1b)**

Compare running times using `compare-sort` between variants of
Quicksort and the
provided implementation of selection sort (`ssort`). Perform two
different comparisons: a comparison between sorting methods using
random permutations of the specified sizes, and a comparison using
already sorted permutations. How do the running times compare to the
asymptotic bounds? How does changing the type of input list change the
relative performance of these algorithms? Note that you may have to
modify the list sizes based on your system memory; compare at least 10
different list sizes. The `print_results` function in `main.py` gives
a table of results, but feel free to use code from Lab 1 to plot
the results as well. 

*Dr. Ding told us to ignore ssort. 

Quicksort and Timsort both have complexity of O(nlogn). Their performance  aligns with the asymptotic bounds, running faster than the worst case for these lists given randomly sorted lists. 

For random permutations of specified sizes, random and fixed pivots ran with similar time complexities of O(nlogn) but Timsort was the fastest although Timsort also has a complexity of O(nlogn). 

For sorted permutations of specified sizes, random pivot ran significantly faster than fixed pivot with Timsort still being the fastest. Qsort with a random pivot had approximately the same runtime for both permutation types while Qsort with a fixed pivot ran significantly slower for sorted permutations of specified sizes. Timsort was the only algorithm that ran noticeably faster for sorted permutations of specified sizes than for random permutations of specified sizes. 

Random pivot generally sorts faster than fixed pivot as we expected. Random permutations of specified list sizes yielded slower performance from both pivot types of quicksort.

Random Permutations of Specified Sizes
|      n |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|--------|---------------------|----------------------|------------|
|    100 |               7.603 |                0.854 |      0.016 |
|    200 |               1.345 |                1.404 |      0.231 |
|    500 |               5.310 |                2.895 |      0.060 |
|   1000 |              10.964 |                8.960 |      0.133 |
|   2000 |              13.533 |              285.002 |      0.364 |
|   5000 |             348.991 |              495.324 |      1.144 |
|  10000 |             551.490 |             1114.636 |      2.203 |
|  20000 |            1991.493 |             1855.082 |     18.207 |
|  50000 |            5850.204 |             6300.409 |    257.235 |
| 100000 |           13720.633 |            13749.907 |    239.236 |

Sorted Permutations of Specified Sizes
|   n |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|-----|---------------------|----------------------|------------|
|  50 |               2.633 |                0.409 |      0.005 |
| 100 |               3.539 |                0.871 |      0.005 |
| 150 |               7.235 |               47.125 |      0.007 |
| 200 |               7.561 |                0.844 |      0.007 |
| 250 |              10.695 |                1.253 |      0.007 |
| 300 |              16.266 |                2.975 |      0.013 |
| 350 |              76.971 |                2.276 |      0.017 |
| 400 |              84.152 |                1.928 |      0.009 |
| 450 |              39.623 |                2.038 |      0.020 |
| 500 |             160.105 |                2.680 |      0.011 |


**1c)**

Python uses a sorting algorithm called [*Timsort*](https://en.wikipedia.org/wiki/Timsort), designed by Tim Peters. Compare the fastest of your sorting implementations to the Python
sorting function `sorted`, conducting the tests in 1b above. 

Timsort and Qsort with a random pivot were the top 2 fastest algorithms; however, timsort consistently ran faster than Qsort by a factor of ~100. 





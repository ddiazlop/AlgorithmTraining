"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

import statistics


class Solution(object):
    def mergesort(self, nums):
        """
        Mergesort

        Divides the array into halves, sorts each half recursively, then merges the sorted halves.
        Always O(n log n) time.
        Stable sort (preserves order of equal elements).
        """
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def heapsort(self, nums):
        """
        Heapsort

        Builds a heap data structure from the array, then repeatedly extracts the maximum (or minimum) to build the sorted array.
        O(n log n) time.
        Not stable.
        """
        import heapq

        heapq.heapify(nums)
        return [heapq.heappop(nums) for _ in range(len(nums))]

    def counting_sort(self, nums):
        """
        Counting Sort

        Only works for integers in a known, limited range.
        Counts occurrences of each value, then reconstructs the sorted array.
        O(n + k) time, where k is the range of input.
        Not comparison-based.
        """
        if not nums:
            return nums
        min_val = min(nums)
        max_val = max(nums)
        count = [0] * (max_val - min_val + 1)
        for num in nums:
            count[num - min_val] += 1
        result = []
        for i, c in enumerate(count):
            result.extend([i + min_val] * c)
        return result

    def radix_sort(self, nums):
        """
        Radix Sort

        Sorts numbers digit by digit (or character by character for strings).
        O(nk) time, where k is the number of digits.
        Only works for integers or strings.
        """
        if not nums:
            return nums
        max_num = max(nums)
        exp = 1
        result = nums[:]
        while max_num // exp > 0:
            result = self._counting_sort_by_digit(result, exp)
            exp *= 10
        return result

    def _counting_sort_by_digit(self, nums, exp):
        n = len(nums)
        output = [0] * n
        count = [0] * 10
        for num in nums:
            index = (num // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            index = (nums[i] // exp) % 10
            output[count[index] - 1] = nums[i]
            count[index] -= 1
        return output

    # O(n log n) complexity
    def quickSort(self, nums):
        """
        Quicksort

        Picks a pivot, partitions the array into elements less than and greater than the pivot, then sorts each partition recursively.
        O(n log n) average, O(n^2) worst-case (rare with good pivot choice).
        Not stable.
        """
        if len(nums) < 1:
            return nums

        pivot = nums[0]
        left = [i for i in nums[1:] if i < pivot]
        right = [i for i in nums[1:] if i > pivot]

        return self.quickSort(left) + [pivot] + self.quickSort(right)

    # Better if arrays are not sorted
    def findMedianSortedArraysQuickSort(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged_lists = nums1 + nums2
        ordered_lists = self.quickSort(merged_lists)

        # Floor division
        middle_index = len(ordered_lists) // 2

        if len(merged_lists) % 2 == 0:
            return (ordered_lists[middle_index - 1] + ordered_lists[middle_index]) / 2
        else:
            return ordered_lists[middle_index]

    # Only works when previous arrays are sorted, we completely avoid sorting.
    # OPTIMAL SOLUTION FOR THIS PROBLEM AS THE TWO ARRAYS ARE ALREADY SORTED.
    def findMedianSortedArraysBinarySearch(self, nums1, nums2):
        """
        Optimized O(log(min(m, n))) solution for finding the median of two sorted arrays.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        # Search range for binary search and half of total length
        imin, imax, half_len_full_array = 0, m, (m + n + 1) // 2
        while imin <= imax:
            # Partinion for nums1 array
            i = (imin + imax) // 2
            # Partition for nums2 array
            j = half_len_full_array - i

            # We need all numbers on the left side of the partition to be less than the right side.
            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                # Correct partition found
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0

    def naive(self, nums1, nums2):
        return statistics.median(sorted(nums1 + nums2))

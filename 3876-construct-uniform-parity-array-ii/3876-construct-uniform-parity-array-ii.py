class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even = [x for x in nums1 if x % 2 == 0]
        odd = [x for x in nums1 if x % 2 != 0]

        if not odd or not even:
            return True

        min_even = min(even)
        min_odd = min(odd)

        if min_even < min_odd:
            return False

        return True
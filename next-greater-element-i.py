class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[0]]
        next_greater = {}

        for i in range(1,len(nums2)):
            if nums2[i] > stack[-1]:
                while stack != [] and nums2[i] > stack[-1]:
                    next_greater[stack.pop(-1)] = nums2[i]

                stack.append(nums2[i])
            else:
                stack.append(nums2[i])
        for i in stack:
            next_greater[i] = -1
            

        for i in range(len(nums1)):
            nums1[i] = next_greater[nums1[i]]

        return nums1

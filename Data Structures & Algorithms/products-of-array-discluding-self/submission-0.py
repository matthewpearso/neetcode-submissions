class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # count zeros
        num_zeroes = 0
        for n in nums:
            if n == 0:
                num_zeroes += 1
        
        # if more than one zero, everything will be zero
        if num_zeroes > 1:
            zero_list = [0] * len(nums)
            return zero_list
        
        # if exactly one zero, that index will be the only non-zero value
        elif num_zeroes == 1:
            value = 1
            for n in nums:
                if n != 0:
                    value = value * n
            output = []
            for n in nums:
                if n == 0:
                    output.append(int(value))
                else:
                    output.append(0)
            return output
        
        else:
            value = 1
            for n in nums:
                value = value * n
            output = []
            for n in nums:
                output.append(int(value / n))
            return output

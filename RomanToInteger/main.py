class Solution:

    #Version one
    def romanToInt(self, s: str) -> int:
        romans_dicts = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_value = 0
        total = 0
        for i in range(len(s) - 1, -1, -1):
            curr_value = romans_dicts[s[i]]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value
        return total

    #version 2 more optimized
    def romanToInt2(s: str) -> int:
        romans_dicts = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_value = 0
        total = 0
        i = len(s) - 1
        while i >= 0:
            curr_value = romans_dicts.get(s[i])
            if curr_value is not None:
                if curr_value < prev_value:
                    total -= curr_value
                else:
                    total += curr_value
                prev_value = curr_value
            else:
                return 0  # or raise an exception for invalid input
            i -= 1
        return total
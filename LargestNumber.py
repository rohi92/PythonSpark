def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        d = []
        for i in nums:
            d.append(str(i))
        k = sorted(d, key=lambda x: x * 10, reverse=True)
        res = ""
        for i in k:
            res += str(i)
        if int(res) == 0:
            return "0"
        return res
if __name__=="__main__":
    print(largestNumber("self", [3,30,34,5,9]))
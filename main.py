def sortColors(self, nums):
    # nums = list(int), don't return anything and just modify nums
    # sort 0, 1, and 2s without any library function
    # strategy: seperate the numbers into 3 different lists and then
    # combine them all into nums at the end?

    # first implementation: 3 lists.
    # beter implementation: 2 lists and prepend ones then append any twos

    zero = []
    one = []
    # two = []

    # for i in nums:
    #     if i == 0:
    #         zero.append(i)
    #     elif i == 1:
    #         one.append(i)
    #     else:
    #         two.append(i)
    for i in nums:
        if i == 0:
            zero.append(i)
        elif i == 1:
            one.insert(0, i)
        else:
            one.append(i)
            
    # nums[:] = list(zero + one + two)
    nums[:] = list(zero + one)

nums = [2, 0, 2, 1, 1, 0]
sortColors(sortColors, nums)
print(nums)
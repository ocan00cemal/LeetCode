import itertools


class Solution:
    def threeSum(self, nums):
        neg_list = []
        pos_list = []
        solution_set = []

        if len(nums) >= 3 and nums[0] == 0 and nums[2] == 0:
            return [[0, 0, 0]]
        elif len(nums) == 0:
            return []
        elif nums[0] == 0:
            return []

        for i in nums:
            if i < 0:
                neg_list.append(i)
            else:
                pos_list.append(i)

        for neg_num in neg_list:
            k = 0
            j = len(pos_list) - 1
            while k < j:
                if pos_list[k] + pos_list[j] == abs(neg_num):
                    solution_set.append([neg_num, pos_list[k], pos_list[j]])
                    k += 1
                    j -= 1

                if pos_list[k] + pos_list[j] > abs(neg_num):
                    j -= 1
                elif pos_list[k] + pos_list[j] < abs(neg_num):
                    k += 1

        for pos_num in pos_list:
            k = 0
            j = len(neg_list) - 1
            while k < j:
                if abs(neg_list[k] + neg_list[j]) == pos_num:
                    solution_set.append([pos_num, neg_list[k], neg_list[j]])
                    k += 1
                    j -= 1

                if abs(neg_list[k] + neg_list[j]) < pos_num:
                    j -= 1
                elif abs(neg_list[k] + neg_list[j]) > pos_num:
                    k += 1

        solution_set.sort()
        solution_set = list(
            solution_set for solution_set, _ in itertools.groupby(solution_set)
        )

        if nums.count(0) >= 3:
            solution_set.append([0, 0, 0])

        return solution_set

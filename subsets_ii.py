# -*- coding: utf-8 -*-

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        ret = []
        S.sort()
        for i in xrange(len(S) + 1):
            combs = self.subsets(S, 0, i) # 计算包含i个元素的子集
            for comb in combs:
                ret.append(comb)
        return ret
        
    def subsets(self, numbers, pos, k):
        n = len(numbers) - pos
        if (not numbers) or (n < k):
            return None
        ret = []
        if k == 0:  # 0/1特殊情况处理
            return [[]]
        for i in xrange(pos, len(numbers), 1):
            if (i > pos) and (numbers[i] == numbers[i - 1]):
                continue
            combs = self.subsets(numbers, i + 1, k - 1)  # 计算i + 1开始位置，包含k - 1个元素的子集
            if combs:
                if combs != [[]]:
                    for comb in combs:
                        new_comb = [numbers[i]]
                        new_comb.extend(comb)
                        ret.append(new_comb)
                else:
                    ret.append([numbers[i]])
        return ret
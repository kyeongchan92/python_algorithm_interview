#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        ordered = defaultdict(list)
        for word in strs:
            ordered[''.join(sorted(word))].append(word)
        return ordered.values()
# @lc code=end

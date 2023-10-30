from typing import List
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_str = ""
        cur_counts = collections.defaultdict(list)
        t_counts = collections.Counter(t)

        for right, x in enumerate(s):
            if x in t and list(t_counts.values()) != [0] * len(t):
                cur_counts[x].append(right)
                t_counts[x] -= 1

            if len(cur_counts) == len(t):
                max_idx = max([x[0] for x in list(cur_counts.values())])
                min_idx = min([x[0] for x in list(cur_counts.values())])
                if min_str == "" or len(min_str) > (max_idx - min_idx + 1):
                    min_str = s[min_idx : max_idx + 1]

                if len(cur_counts[s[min_idx]]) > 1:
                    cur_counts[s[min_idx]].pop(0)
                else:
                    cur_counts.pop(s[min_idx])
                t_counts[s[min_idx]] += 1

        return min_str
    

print(Solution().minWindow(s = "aa", t = "aa"))

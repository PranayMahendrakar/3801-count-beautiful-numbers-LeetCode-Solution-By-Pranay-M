class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def count(n):
            if n <= 0:
                return 0
            s = str(n)
            from functools import lru_cache
            
            @lru_cache(maxsize=None)
            def dp(pos, prod, dsum, tight, started):
                if pos == len(s):
                    if not started:
                        return 0
                    if dsum == 0:
                        return 0
                    return 1 if prod % dsum == 0 else 0
                
                limit = int(s[pos]) if tight else 9
                res = 0
                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)
                    if not started and d == 0:
                        res += dp(pos + 1, 0, 0, new_tight, False)
                    else:
                        new_prod = prod * d if started else d
                        new_sum = dsum + d
                        res += dp(pos + 1, new_prod, new_sum, new_tight, True)
                return res
            
            return dp(0, 0, 0, True, False)
        
        return count(r) - count(l - 1)
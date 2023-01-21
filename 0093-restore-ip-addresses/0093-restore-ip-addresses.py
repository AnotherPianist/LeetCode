class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def dfs(i, formed):
            if i == len(s):
                if len(formed) == 4:
                    res.append('.'.join(map(str, formed)))
                return
            
            if formed[-1] != 0 and formed[-1] * 10 + int(s[i]) <= 255:
                last_item = formed[-1]
                formed[-1] = last_item * 10 + int(s[i])
                dfs(i + 1, formed)
                formed[-1] = last_item
            
            if len(formed) < 4:
                dfs(i + 1, formed + [int(s[i])])
        
        dfs(1, [int(s[0])])

        return res
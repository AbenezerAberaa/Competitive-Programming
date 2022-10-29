class Solution:
    def reverseParentheses(self, s: str) -> str:
        container = []
        lookup_dict = {}
        for i, c in enumerate(s):
            if c == '(':
                container.append(i)
            elif c == ')':
                j = container.pop()
                lookup_dict[i] = j
                lookup_dict[j] = i
        result = []
        i = 0
        d = 1
        while i < len(s):
            if i in lookup_dict:
                i = lookup_dict[i]
                d *= -1
            else:
                result.append(s[i])
            i += d
        return "".join(result)
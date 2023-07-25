class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        dict_one = {}
        dict_two = {}
        for i, ch in enumerate(s1):
            if ch not in dict_one:
                dict_one[ch] = [s2[i]]
            else:
                dict_one[ch].append(s2[i])
            if s2[i] not in dict_two:
                dict_two[s2[i]] = [ch]
            else:
                dict_two[s2[i]].append(ch)  
        
        unions = []
        used = set()
        for ch in dict_one:
            if ch in used:
                continue

            lake = set(ch)
            for s_el in dict_one[ch]:
                lake.add(s_el)
            visited = set()

            while lake-visited:
                for el in list(lake-visited):
                    if el in dict_one:
                        for ch in dict_one[el]:
                            lake.add(ch)
                    if el in dict_two:
                        for ch in dict_two[el]:
                            lake.add(ch)
                    visited.add(el)
            
            used = used | visited
            unions.append(visited)
        answer = []
        for ch in baseStr:
            for u in unions:
                if ch in u:
                    answer.append(sorted(list(u))[0])
                    break
            else:
                answer.append(ch)
        return "".join(answer)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []
        used = set()

        x = 0

        while x < len(strs):
            if x in used:
                x += 1
                continue

            group.append([strs[x]])
            used.add(x)

            y = x + 1

            while y < len(strs):
                if y not in used and self.Anagrams(strs[x], strs[y]):
                    group[-1].append(strs[y])
                    used.add(y)

                y += 1

            x += 1

        return group

    def Anagrams(self, x, y):
        if len(x) != len(y):
            return False

        count = {}

        for i in range(len(x)):
            count[x[i]] = 1 + count.get(x[i], 0)
            count[y[i]] = count.get(y[i], 0) - 1

        for char in count:
            if count[char] != 0:
                return False

        return True
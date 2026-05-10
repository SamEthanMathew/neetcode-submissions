class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pairs = []

        for num in nums:
            found = False

            for pair in pairs:
                if pair[0] == num:
                    pair[1] += 1
                    found = True
                    break

            if found == False:
                pairs.append([num, 1])

        pairs.sort(key=lambda pair: pair[1], reverse=True)

        result = []
        for i in range(k):
            result.append(pairs[i][0])

        return result
            




        
        
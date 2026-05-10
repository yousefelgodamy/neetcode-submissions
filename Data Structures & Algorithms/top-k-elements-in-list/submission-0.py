class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int) # num to count
        for num in nums:
            counts[num] += 1

        heap_items = [(-count[1], count[0]) for count in counts.items()]
        heapq.heapify(heap_items)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap_items)[1])

        return result
import heapq

class GreedyDualCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.L = 0.0  # global aging level
        self.cache = {}  # key -> H value
        self.heap = []   # min-heap of (H, key)
    
    def access(self, key, cost):
        if key in self.cache:
            # Update priority for existing key
            self.cache[key] = self.L + cost
            heapq.heappush(self.heap, (self.cache[key], key))
        else:
            if len(self.cache) >= self.capacity:
                # Evict min H item
                while True:
                    H, evict_key = heapq.heappop(self.heap)
                    if self.cache.get(evict_key, None) == H:
                        break
                self.L = self.cache.pop(evict_key)
            # Add new key
            self.cache[key] = self.L + cost
            heapq.heappush(self.heap, (self.cache[key], key))

# Example usage
if __name__ == "__main__":
    cache = GreedyDualCache(capacity=3)
    accesses = [("A", 1), ("B", 5), ("C", 2), ("D", 3), ("B", 5)]
    for key, cost in accesses:
        cache.access(key, cost)
        print("Cache state:", cache.cache)

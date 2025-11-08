from concurrent.futures import ThreadPoolExecutor

def parallel_search(predicate, shards):
    """
    Divide-and-Conquer Parallel Search
    Input:
        predicate : function returning True/False for each item
        shards    : list of lists (data partitions)
    Output:
        set of items satisfying predicate
    """
    def scan_shard(shard):
        return [x for x in shard if predicate(x)]
    
    with ThreadPoolExecutor() as executor:
        results = executor.map(scan_shard, shards)
    
    # merge partial results
    return {item for sublist in results for item in sublist}

# Example usage
if __name__ == "__main__":
    shards = [
        [1, 3, 5, 7],
        [2, 4, 6, 8]
    ]
    is_even = lambda x: x % 2 == 0
    matching = parallel_search(is_even, shards)
    print("Even numbers:", matching)

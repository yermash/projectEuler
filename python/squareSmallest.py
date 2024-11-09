import heapq


def squareSmallest(n, m):
    nums = list(range(2, n + 1))
    heapq.heapify(nums)

    for _ in range(m):
        smallest = heapq.heappop(nums)
        heapq.heappush(nums, smallest ** 2)

    # Calculate the sum modulo 1234567891
    return sum(nums) % 1234567891

print(squareSmallest(10**4, 10**16))
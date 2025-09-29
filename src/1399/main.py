class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = {}
        for i in range(1, n + 1):
            num_digits = sum(int(x) for x in str(i))
            print(counts, i, num_digits, str(i))
            if num_digits not in counts:
                counts[num_digits] = 1
            else:
                counts[num_digits] += 1
        
        max_count = max(counts.values())
        num_max_counts = sum(1 for count in counts.values() if count == max_count)
        print(counts, max_count, num_max_counts)
        return num_max_counts

        
    
if __name__ == "__main__":
    s = Solution()
    calc = s.countLargestGroup(24)  # Output: 4
    assert calc == 5
    
    print()
    
    calc = s.countLargestGroup(2)
    assert calc == 2
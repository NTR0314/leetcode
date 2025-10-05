from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        D = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        rpac = []
        unvisited_pac = [(x, y) for x in range(len(heights)) for y in [0]] + \
            [(x, y) for x in [0] for y in range(len(heights[0]))]
        ratl = []
        unvisited_atl = [(x, y) for x in range(len(heights)) for y in [len(heights[0]) - 1]] + \
            [(x, y) for x in [len(heights) - 1] for y in range(len(heights[0]))]
            
        while unvisited_pac:
            cx, cy = unvisited_pac.pop()
            rpac.append((cx, cy))
            for dx, dy in D:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]) and \
                        (nx, ny) not in rpac and (nx, ny) not in unvisited_pac and \
                        heights[nx][ny] >= heights[cx][cy]:
                            rpac.append((nx, ny))
                            unvisited_pac.append((nx, ny))
        while unvisited_atl:
            cx, cy = unvisited_atl.pop()
            ratl.append((cx, cy))
            for dx, dy in D:
                nx, ny = cx + dx, cy + dy
                # if (nx, ny) == (3, 0) and (cx, cy) == (4, 0):
                #     breakpoint()
                if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]) and \
                        (nx, ny) not in ratl and (nx, ny) not in unvisited_atl and \
                        heights[nx][ny] >= heights[cx][cy]:
                            ratl.append((nx, ny))
                            unvisited_atl.append((nx, ny))
        
        res = list(set(rpac) & set(ratl))
        res.sort()
        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
                    
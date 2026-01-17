class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side=0
        for i in range(n):
            for j in range(i+1,n):
                ax1,ay1=bottomLeft[i]
                ax2,ay2=topRight[i]

                bx1,by1=bottomLeft[j]
                bx2,by2=topRight[j]

                inter_left_x = max(ax1,bx1)
                inter_left_y = max(ay1,by1)
                inter_right_x = min(ax2,bx2)
                inter_right_y = min(ay2,by2)

                side_x = inter_right_x - inter_left_x
                side_y = inter_right_y - inter_left_y

                side = min(side_x,side_y)
                max_side = max(max_side,side)
        return max_side*max_side

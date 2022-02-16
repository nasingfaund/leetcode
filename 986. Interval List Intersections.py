class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        first = second = 0
        while first < len(firstList) and second < len(secondList):
            if firstList[first][0] <= secondList[second][1] and firstList[first][1] >= secondList[second][0]:
                start = max(firstList[first][0], secondList[second][0])
                end = min(firstList[first][1], secondList[second][1])

                intersections.append([start, end])
                
            if firstList[first][1] < secondList[second][1]:
                first +=1
            else:
                second +=1
          
        return intersections

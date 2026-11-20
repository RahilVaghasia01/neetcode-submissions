class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]
        newArray = [0] * len(arr)
        newArray[-1] = -1

        for i in reversed(range(0, len(arr) - 1,)) :
            newArray[i] = greatest
            if(arr[i] > greatest) :
                greatest = arr[i]
        return newArray
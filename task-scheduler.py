class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = []
        for i in tasks:
            if ord(i) - 65 >= len(frequency):
                frequency += [0]*((ord(i)-64)-len(frequency))
            frequency[ord(i)-65] += 1
        frequency.sort(reverse = True)

        space = 0
        i=0
        print(frequency[0])
        print(frequency)
        print(len(tasks))
        while i < len(frequency) and n != 0:
            space += (frequency[i]-1)*n
            minspace = space//n 
            i+=1
            while i < len(frequency):
                if frequency[i] > minspace :
                    space -= minspace  + (frequency[i] - minspace -1)*n
                else: space -= frequency[i]
                i += 1
                print(space)
        space = max(space, 0)
        return int(space + len(tasks))

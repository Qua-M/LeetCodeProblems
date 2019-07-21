class Solution:
    
    def distributeCandies(self, candies, num_people):
        added = 1
        people = [0]
        people *= num_people
        while candies > 0:
            for i in range(len(people)):
                if candies - added > 0:
                    people[i] += added
                    candies -= added
                    added += 1
                else:
                    people[i] += candies
                    candies -= candies
        return(people)tributeCandies(7, 4)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        '''
        How would I do this, intuitively?

        Start at any prerequisites entry. Look at the course on the right.

        Check to see if that course exists as the LEFT element anywhere else. If not, then I can just take it. This means I can now take the original one on the left.

        To track what prereqs I have met, I can keep another array, called "taken"

        I will see, for each right entry if it is met. Otherwise, I will continue going.

        alternatively, if i start at some point, I can treat it as the start of a path. If this path is a cycle, then I can label it as impossible. The issue is that there can be disjoint courses, so I will need to still track what courses are taken. This approach is not going to work if a class has 2 prereqs. plus searching i sslow.

        we will ASSUME i can just take every class I see. We are going to start randomly, and take the course. Then we will add its prereqs to a stack. If we can take those, then we do, otherwise we assume we can and add their prereqs. If we ever try to add a prereq to the stack that is already in "taken", then we are cooked.

        In what case do we hit a "false" -> when there is a cycle. All other cases are okay. So, we just need to see if there is a cycle.
        
        we can keep a log of what we have seen, starting at some point and looking for the end. if we ever run into something we already saw, we know there was a cycle.

        '''

        reqs = {i: [] for i in range(numCourses)}
        for course, prereqs in prerequisites:
            reqs[course].append(prereqs)

        

        # now that we have this, we need the search function
        # it is going to check if each one
        visited = set()

        def dfs(course):
            if (course in visited):
                return False
            if reqs[course] == []:
                return True
            
            visited.add(course)
            for prereq in reqs[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            reqs[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True




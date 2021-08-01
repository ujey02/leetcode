class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        schedule = {}
        self.prereq ={}
        
        for i in range(numCourses):
            self.prereq[i] = []
        
        for course in prerequisites:
            course_num, pre_num = course
            self.prereq[course_num].append(pre_num)
            
        order = []
        
        def courseToTake(idx):
            #print("course to take: ", idx)
            if self.prereq[idx] == 0: #already taken
                return []
            elif self.prereq[idx] == -1: #currently on a loop...
                return -1
            elif self.prereq[idx] == []: #no prerequisite
                self.prereq[idx] = 0
                return [idx]
            else:
                courses = []
                prereqs = self.prereq[idx]
                self.prereq[idx] = -1
                
                for p in prereqs:
                    allPrereqs = courseToTake(p)
                    if allPrereqs == -1:
                        return -1
                    else:
                        courses += allPrereqs
                    # print (courses)
                self.prereq[idx] = 0
                return courses + [idx]
                
        
        for i in range(numCourses):
            courses = courseToTake(i)
            if courses == -1:
                return []
            order += courses
        
        return order
                
            
        

#Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] Output: [0,2,1,3]
#Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] Output: [0,2,1,3]

order_list=[]
def bfs(dict,order_list,course_id):
    try:
        for i in course_id[1]:
            if i not in order_list and course_id[0] not in order_list:
                order_list.append(i)
                order_list.append(course_id[0])

            elif i not in order_list and course_id[0] in order_list:
                index = order_list.index(i)
                order_list.insert(index - 1, i)
                bfs(dict, order_list, (i, dict[i]))
            elif i in order_list and course_id[0] not in order_list:
                index = order_list.index(i)
                order_list.insert(index+1,course_id[0])

    except:
        return [0]








def order(prerequisites,numCourses,dict):
    try:


        for k,v in dict.items():
            bfs(dict,order_list,(k,v))
        return order_list
    except:
        return [0]





if __name__=="__main__":
    numCourses , prerequisites =1, [[1,0],[2,0],[3,1],[3,2]]
    dict={}
    try:

        for i in prerequisites:
            try:
                dict[i[0]].append(i[1])
            except:
                dict[i[0]]=[i[1]]
        print(order(prerequisites, numCourses, dict))
    except:
        dict={}
        print(order(prerequisites,numCourses,dict))





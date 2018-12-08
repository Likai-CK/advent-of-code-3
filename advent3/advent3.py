
def is_overlapping(list_of_confirmed_points, point_to_check):
    for point in list_of_confirmed_points:
        #print(point)
        #print(point_to_check)
        if(point == point_to_check):
            return True
    return False

if __name__ == "__main__":

    print(is_overlapping([[1,2]],[1,2]))
    file = open("puzzle.txt", "r")
    lines = file.read()
    lines = lines.split()
    print("\n")
    print(lines[0])
    print(lines[1])
    print(lines[2])
    print(lines[3])
    
    index = 0
    spot = 0
    last_point = []
    point_list = []
    overlapping_sqr_inches = 0
    
    spot = 1
    print("LENGTH:")
    print(str(len(lines)))

    for i in lines:
        if(spot == 3):
            last_point = i.strip(":").split(",")
            last_point[0] = int(last_point[0])
            last_point[1] = int(last_point[1])
            #print("LAST POINT")
            #print(last_point)
        elif(spot == 4):
            dimensions_x = int(i.split("x")[0])
            dimensions_y = int(i.split("x")[1])
            #print("HERE")
            #print(dimensions_y)
            endpoint_up_left = last_point
            endpoint_up_right =  [int(last_point[0]) + dimensions_x, int(last_point[1])]
            endpoint_down_left = [int(last_point[0]), int(last_point[1]) - dimensions_y]
            endpoint_down_right = [int(last_point[0]) + dimensions_x, int(last_point[1]) - dimensions_y]
            for x in range(last_point[0],endpoint_up_right[0]): # low x to high x
                for y in range(endpoint_down_right[1],last_point[1] ): # high y to low y
                    #print([x,y])
                    # at this point, there is a list of points in point_list [[x,y], [x,y].....]
                    # likewise, last_point contains the last origin point for the next shape, representing the upper
                    # left of the rectangle.
                    # The dimensions are calculated afteward, and the points in each spot of that shape are what is being
                    # put into this array.
                    #print(is_overlapping(point_list, [x,y]))
                    if(is_overlapping(point_list, [x,y])):
                        overlapping_sqr_inches = overlapping_sqr_inches + 1
                    else:
                        point_list.append([x,y])
            spot = 0
        print(overlapping_sqr_inches)
        spot = spot + 1

    #print(str(len(point_list)))
    #iters = 0
    #for point in point_list:
    #    
    #    if(is_overlapping(point_list, point)):s
    #        overlapping_sqr_inches = overlapping_sqr_inches + 1
    #        iters = iters + 1
    #    #else:
    #        #print("not overlapping.")
    #
    # print(point_list)
    print(overlapping_sqr_inches)
         

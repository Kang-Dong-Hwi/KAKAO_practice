
def OK ( point ):
    for x,y,cr in point:
        #x,y,cr = i[0], i[1], i[2]
        if(cr == 0): # 기둥
            if(y == 0  or  [x,y,1] in point  or  [x-1,y,1] in point
            or  [x,y-1,0] in point  or  [x,y,0] not in point):
                continue
            else:    return False

        if(cr == 1): #보
            if([x,y-1,0] in point  or  [x+1,y-1,0] in point  or
            ( [x-1,y,1] in point and  [x+1,y,1] in point )  or  [x,y,1] not in point ):
                continue
            else:    return False
    return True

def solution(n, build_frame):
    point = []
    for x,y,z,det in build_frame:

        if(det==1):
            point.append([x,y,z])
            if( OK(point) == False ):
                point.pop()
        else:
            if([x,y,z] in point):
                point.remove([x,y,z])
                if( OK(point) == False ):
                    point.append([x,y,z])

    point.sort()
    return point

"""
기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나,
 또는 다른 기둥 위에 있어야 합니다.

보는 한쪽 끝 부분이 기둥 위에 있거나,
또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
"""
print(solution())

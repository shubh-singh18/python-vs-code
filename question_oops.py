# write can create and view 2D coordinates
#.>A user can find out the distance between 2 coordinates
#.>A user can find the distance of a coordinates from origin
#.>A user can check if a point on a given line.
#.>A user can find the distance between a given 2D point and a given line

class Point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y

    def __str__(self):
       return '<{},{}>'.format(self.x_cod,self.y_cod)

    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5


    def distance_from_origin(self):
       return (self.x_cod**2 + self.y_cod**2)**0.5

class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y +{} =0'.format(self.A,self.B,self.C)

    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C==0:
            return "lies on the line"
        else:
            return "does not lie on the line"

    def shortest_distance(line,point):
        abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)**0.5
        

# p1=Point(0,0)
# p2=Point(10,10)
# print(p1.euclidean_distance(p2))
# print(p1.distance_from_origin())

l1=Line(3,4,5)
p1 =Point(1,2)
print(l1)
print(p1)
l1.shortest_distance(p1)


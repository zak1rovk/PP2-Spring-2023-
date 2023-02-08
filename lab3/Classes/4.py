class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f'{Point(self.x,self.y)}')
    def move(self, delta_x, delta_y):
        self.x+=delta_x
        self.y+=delta_y
    def dist(self, end_point):
        dist_x=self.x-end_point.x
        dist_y=self.y-end_point.y
        return (dist_x**2+dist_y**2)**0.5
    
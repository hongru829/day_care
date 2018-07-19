
# Given a robot cleaner in a room modeled as a grid. Each cell in the grid can be empty or
# blocked. The robot cleaner can move forward, turn left or turn right.
# When it tries to move into a blocked cell,
# its bumper sensor detects the obstacle and it stays on the current cell.


# The control API:

# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cell.
#   boolean Move();

#   // Robot will stay on the same cell after calling Turn*. k indicates how
#   // many turns to perform.
#   void TurnLeft(int k);
#   void TurnRight(int k);

#   // Clean the current cell.
#   void Clean();

#   boolean Move(Direction d);
# }

# sample input
# ++++++++++
# +........+
# +...^....+
# +.+......+
# ++++.+++++

# +.....+
# +++++++
# 要求用给定的API打扫完所有empty格子。. 一亩-三分-地，独家发布

# 楼主一开始想用bfs做，后来发现我连robot的位置都不知道。。. Waral 博客有更多文章,

# 于是面试官简化
# 简化1：robot自己可以知道自己当前的位置。就是两个新API：robot.x(), robot.y()

# 楼主到这里还是一脸懵逼，于是面试官又提示：你怎样让robot从一个点走到格子里的另一个点。

# 楼主最后磕磕绊绊把最后一个提示想出思路来了，但是没写完就到时间了。. Waral 博客有更多文章,
#
# 权当攒人品吧。。。

Class Roomb {
  //Given API
  boolean move()

  void turnLeft()
  void turnRight()
  void clean()

  Class Coordinate {
    int x,
    int y
    public Coordinate(int x, int y) {
      this.x = x
      this.y = y
    }

    public boolean equals(Object obj) {
      if (this == obj) {
        return true;
      }
      if (!(obj instanceof Coordinate)) return false;
      Coordinate coor = (Coordinate) obj;
      return this.x == coor.x && this.y == coor.y;
    }
    //reduce collision
    publc int hasCode() {
      return 100003*x + y
    }
  }


  int curDir = 0
  //initial default Direction is 'up'
  int[][] dir = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
  Set<Coordinate> visited;

  public Roomba() {
    newStart()
  }

  public void newStart() {

  }

}












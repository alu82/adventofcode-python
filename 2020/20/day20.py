import os
import time
import math

SEA_MONSTER = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

class Geometry:
    def __init__(self, image):
        self.image = image

    def rotate(self):
        rotated_image = []
        col_size = len(self.image)
        row_size = len(self.image[0])
        for row in range(row_size):
            line = ""
            for col in range(col_size):
                line += self.image[col][row_size-row-1]
            rotated_image.append(line)
        self.image = rotated_image

    def flip_x(self):
        flipped_image = []
        size = len(self.image)
        for n in range(size):
            flipped_image.append(self.image[size-n-1])
        self.image = flipped_image
    
class Tile(Geometry):
    def __init__(self, raw_tile):
        super().__init__(raw_tile[1:])
        self.name = int(raw_tile[0][5:-1])
        self.inner_imgage = []
        self.borders = []
        self.update()
        
    def update(self):
        # inner image
        new_inner_image = []
        for l in range(1,len(self.image)-1):
            new_inner_image.append(self.image[l][1:-1])
        self.inner_image = new_inner_image
        # borders convention for border index: 0 upper, 1 right, 2 lower, 3 left
        new_borders = []
        new_borders.append(self.image[0])
        new_borders.append("".join([line[-1] for line in self.image]))
        new_borders.append(self.image[-1])
        new_borders.append("".join([line[0] for line in self.image]))
        self.borders = new_borders
    
    def rotate(self):
        super().rotate()
        self.update()

    def flip_x(self):
        super().flip_x()
        self.update()

    def get_all_possible_borders(self):
        return self.borders + [b[::-1] for b in self.borders]

class Sea_Monster(Geometry):
    def __init__(self):
        super().__init__(SEA_MONSTER)
        self.relative_pos = self.get_relative_pos()

    def get_relative_pos(self):
        first = None
        rel_pos = set()
        for row in range(len(self.image)):
            for col in range(len(self.image[row])):
                if self.image[row][col] == "#":
                    if first is None:
                        first = (row, col)
                        new_pos = (0,0)       
                    else:
                        r, c = first
                        new_pos = (row - r, col - c)
                    rel_pos.add(new_pos)
        return rel_pos
   
def solve_1(input):
    tiles = [Tile(t) for t in input]
    edges = get_edges(tiles)
    return math.prod([e.name for e in edges])
    
def solve_2(input):
    tiles = [Tile(t) for t in input]
    size = int(math.sqrt(len(tiles)))
    tile_grid = [size*[None] for _ in range(size)]
    remaining_tiles = set(tiles)
    for row in range(size):
        for col in range(size):
            if row == 0 and col == 0:
                edge = get_left_upper_tile(tiles)
                tile_grid[row][col] = edge
                remaining_tiles.remove(edge)
            else:
                fitting_tiles = get_fitting_tiles(tile_grid, row, col, remaining_tiles)
                if len(fitting_tiles) > 0:
                    edge = fitting_tiles.pop()
                    tile_grid[row][col] = edge
                    remaining_tiles.remove(edge)
    
    complete_image = Geometry(get_actual_image(tile_grid))
    n_monsters = find_monsters(complete_image)
    size_monster = sum([m.count("#") for m in SEA_MONSTER]) 
    total_monster = n_monsters*size_monster
    return sum([l.count("#") for l in complete_image.image]) - total_monster

def find_monsters(complete_image):
    monster = Sea_Monster()
    size = len(complete_image.image)
  
    for n in range(8):
        n_monster = 0
        for row in range(size):
            for col in range(size):
                if is_monster(complete_image, monster, row, col):
                    n_monster += 1
        if n_monster > 0:
            return n_monster

        # change image /rotate/flip
        if n == 4:
            complete_image.flip_x()
        complete_image.rotate()
    return 0
    

def is_monster(complete_image, monster, row, col):
    size = len(complete_image.image)
    for pos in monster.relative_pos:
        row_ = row + pos[0]
        col_ = col + pos[1]
        if (row_ < 0 or row_ >= size) or (col_ < 0 or col_ >= size):
            return False
        if complete_image.image[row_][col_] != "#":
            return False
    return True

def get_actual_image(image):
    actual_image = []
    for row in range(len(image)):
        row_imgs = []
        for col in range(len(image)):
            row_imgs.append(image[row][col].inner_image)
        
        size = len(row_imgs[0])
        for l in range(size):
            line = ""
            for img in row_imgs:
                line += img[l]
            actual_image.append(line)
    return actual_image
    
def get_fitting_tiles(tile_grid, row, col, remaining_tiles):
    fitting_tiles = set()
    neighbor_borders = get_neighbor_borders(tile_grid, row, col)
    for r_tile in remaining_tiles:
        for n in range(9):
            fits = all([neighbor_borders[n] == r_tile.borders[n] for n in range(len(neighbor_borders)) if neighbor_borders[n] is not None])
            if fits:
                fitting_tiles.add(r_tile)
                break
            if n == 4:
                r_tile.flip_x()
            r_tile.rotate()
    return fitting_tiles

def get_neighbor_borders(tile_grid, row, col):
    size = len(tile_grid)
    neighbor_borders = [None, None, None, None]
    # Upper Neighbor
    row_ = row-1
    col_ = col
    if 0 <= row_ < size and 0 <= col_ < size:
        if tile_grid[row_][col_] is not None:
            neighbor = tile_grid[row_][col_]
            neighbor_borders[0] = neighbor.borders[2]
    # right Neighbor
    row_ = row
    col_ = col+1
    if 0 <= row_ < size and 0 <= col_ < size:
        if tile_grid[row_][col_] is not None:
            neighbor = tile_grid[row_][col_]
            neighbor_borders[1] = neighbor.borders[3]  
    # lower Neighbor
    row_ = row+1
    col_ = col
    if 0 <= row_ < size and 0 <= col_ < size:
        if tile_grid[row_][col_] is not None:
            neighbor = tile_grid[row_][col_]
            neighbor_borders[2] = neighbor.borders[0] 
    # left Neighbor
    row_ = row
    col_ = col-1
    if 0 <= row_ < size and 0 <= col_ < size:
        if tile_grid[row_][col_] is not None:
            neighbor = tile_grid[row_][col_]
            neighbor_borders[3] = neighbor.borders[1]
    return neighbor_borders

def get_left_upper_tile(tiles):
    tile = get_edges(tiles)[0]
    for n in range(8):
        if n%4 == 0:
            tile.flip_x()
        tile.rotate()

        my_borders = set([tile.borders[0], tile.borders[3]])
        other_borders = set()
        for other_tile in tiles:
            if other_tile != tile:
                for ob in other_tile.get_all_possible_borders():
                    other_borders.add(ob)
        
        if len(my_borders.intersection(other_borders)) == 0:
            return tile

def get_edges(tiles):
    edges = []
    for tile in tiles:
        my_borders = set(tile.get_all_possible_borders())
        other_borders = set()
        for other_tile in tiles:
            if other_tile != tile:
                for ob in other_tile.get_all_possible_borders():
                    other_borders.add(ob)

        if len(my_borders.intersection(other_borders)) == 4: # 4 because every border is counted twice
            edges.append(tile)
    return edges

with open(os.path.dirname(__file__) + "/input", "r") as myInput:
    start_time = time.time()
    input = [block.splitlines() for block in myInput.read().split("\n\n")]
    print(solve_1(input))
    print(solve_2(input))
    print("--- Execution time %s s ---" % (time.time() - start_time))

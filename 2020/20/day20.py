import os
import time
import math

SEA_MONSTER = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

class Sea_Monster:
    def __init__(self):
        self.img = SEA_MONSTER
        self.relative_pos()

    def relative_pos(self):
        first = None
        rel_pos = set()
        for row in range(len(self.img)):
            for col in range(len(self.img[row])):
                if self.img[row][col] == "#":
                    if first is None:
                        first = (row, col)
                        new_pos = (0,0)
                        
                    else:
                        r, c = first
                        new_pos = (row - r, col - c)
                    rel_pos.add(new_pos)
        self.relative = rel_pos

def flip_x(image):
    flipped_image = []
    size = len(image)
    for n in range(size):
        flipped_image.append(image[size-n-1])
    return flipped_image

def rotate(image):
    rotated_image = []
    col_size = len(image)
    row_size = len(image[0])
    for row in range(row_size):
        line = ""
        for col in range(col_size):
            line += image[col][row_size-row-1]
        rotated_image.append(line)
    return rotated_image
    
class Tile:
    def __init__(self, raw_tile):
        self.name = int(raw_tile[0][5:-1])
        self.raw_image = raw_tile[1:]
        self.imgage = []
        self.borders = []
        self.update()
        
    def update(self):
        # actual image
        actual_image = []
        for l in range(1,len(self.raw_image)-1):
            actual_image.append(self.raw_image[l][1:-1])
        self.image = actual_image
        # borders convention for border index: 0 upper, 1 right, 2 lower, 3 left
        new_borders = []
        new_borders.append(self.raw_image[0])
        new_borders.append("".join([line[-1] for line in self.raw_image]))
        new_borders.append(self.raw_image[-1])
        new_borders.append("".join([line[0] for line in self.raw_image]))
        self.borders = new_borders

    def get_all_possible_borders(self):
        return self.borders + [b[::-1] for b in self.borders]
       
    def rotate(self):
        rotated_image = []
        col_size = len(self.raw_image)
        row_size = len(self.raw_image[0])
        for row in range(row_size):
            line = ""
            for col in range(col_size):
                line += self.raw_image[col][row_size-row-1]
            rotated_image.append(line)
        self.raw_image = rotated_image
        self.update()

    def flip_x(self):
        flipped_image = []
        size = len(self.raw_image)
        for n in range(size):
            flipped_image.append(self.raw_image[size-n-1])
        self.raw_image = flipped_image
        self.update()
    
    def __str__(self):
        image = str(self.name)
        for l in self.raw_image:
            image += "\n" + l
        return image
      
def solve_1(input):
    tiles = [Tile(t) for t in input]
    edges = get_edges(tiles)
    return math.prod([e.name for e in edges])
    
def solve_2(input):
    tiles = [Tile(t) for t in input]
    size = int(math.sqrt(len(tiles)))
    image = [size*[None] for _ in range(size)]
    remaining_tiles = set(tiles)
    for row in range(size):
        for col in range(size):
            if row == 0 and col == 0:
                edge = get_left_upper_tile(tiles)
                image[row][col] = edge
                remaining_tiles.remove(edge)
            else:
                fitting_tiles = get_fitting_tiles(image, row, col, remaining_tiles)
                if len(fitting_tiles) > 0:
                    edge = fitting_tiles.pop()
                    image[row][col] = edge
                    remaining_tiles.remove(edge)
    
    actual_image = get_actual_image(image)
    n_monsters = find_monsters(actual_image)
    size_monster = 15
    total_monster = n_monsters*size_monster
    return sum([l.count("#") for l in actual_image]) - total_monster

def find_monsters(image):
    monster = Sea_Monster()
    size = len(image)
  
    for n in range(8):
        n_monster = 0
        for row in range(size):
            for col in range(size):
                if is_monster(image, monster, row, col):
                    n_monster += 1
        if n_monster > 0:
            return n_monster

        # change image /rotate/flip
        if n == 4:
            image = flip_x(image)
        image = rotate(image)
    return 0
    

def is_monster(image, monster, row, col):
    size = len(image)
    for pos in monster.relative:
        row_ = row + pos[0]
        col_ = col + pos[1]
        if (row_ < 0 or row_ >= size) or (col_ < 0 or col_ >= size):
            return False
        if image[row_][col_] != "#":
            return False
    return True

def get_actual_image(image):
    actual_image = []
    for row in range(len(image)):
        row_imgs = []
        for col in range(len(image)):
            row_imgs.append(image[row][col].image)
        
        size = len(row_imgs[0])
        for l in range(size):
            line = ""
            for img in row_imgs:
                line += img[l]
            actual_image.append(line)
    return actual_image
    
def get_fitting_tiles(image, row, col, remaining_tiles):
    fitting_tiles = set()
    neighbor_borders = get_neighbor_borders(image, row, col)
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

def get_neighbor_borders(image, row, col):
    size = len(image)
    neighbor_borders = [None, None, None, None]
    # Upper Neighbor
    row_ = row-1
    col_ = col
    if 0 <= row_ < size and 0 <= col_ < size:
        if image[row_][col_] is not None:
            neighbor = image[row_][col_]
            neighbor_borders[0] = neighbor.borders[2]
    # right Neighbor
    row_ = row
    col_ = col+1
    if 0 <= row_ < size and 0 <= col_ < size:
        if image[row_][col_] is not None:
            neighbor = image[row_][col_]
            neighbor_borders[1] = neighbor.borders[3]  
    # lower Neighbor
    row_ = row+1
    col_ = col
    if 0 <= row_ < size and 0 <= col_ < size:
        if image[row_][col_] is not None:
            neighbor = image[row_][col_]
            neighbor_borders[2] = neighbor.borders[0] 
    # left Neighbor
    row_ = row
    col_ = col-1
    if 0 <= row_ < size and 0 <= col_ < size:
        if image[row_][col_] is not None:
            neighbor = image[row_][col_]
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

        if len(my_borders.intersection(other_borders)) == 4: # 4 because every border is doubled
            edges.append(tile)
    return edges


with open(os.path.dirname(__file__) + "/input", "r") as myInput:
    start_time = time.time()
    input = [block.splitlines() for block in myInput.read().split("\n\n")]
    print(solve_1(input))
    print(solve_2(input))
    print("--- Execution time %s s ---" % (time.time() - start_time))

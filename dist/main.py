import collections

import numpy as np

field_size = 1000


def parse_line(line):
    line_list = line.split()
    line_id = line_list[0].strip("#")
    coords = line_list[2].strip(":").split(",")
    dim = line_list[3].split("x")
    return line_id, coords, dim


if __name__ == "__main__":
    field = np.zeros(shape=(field_size, field_size))
    with open("input.txt") as fp:
        lines = fp.readlines()

    for line in lines:
        line_id, coords, dim = parse_line(line)
        coords_x, coords_y = int(coords[0]), int(coords[1])
        dim_x, dim_y = int(dim[0]), int(dim[1])
        field[coords_y:coords_y + dim_y, coords_x:coords_x + dim_x] += 1
    print("answer phase 1:")
    print(len(field[np.where(field >= 2)]))

    for line in lines:
        line_id, coords, dim = parse_line(line)
        coords_x, coords_y = int(coords[0]), int(coords[1])
        dim_x, dim_y = int(dim[0]), int(dim[1])
        if np.all(field[coords_y:coords_y + dim_y, coords_x:coords_x + dim_x] == 1):
            print("answer phase 2:")
            print(line_id)

import math
from math import pi


def main():
    result_square = ""
    result_rectangle = ""
    result_circle = ""
    with open("input.txt", "r") as f:
        read_content = f.readlines()
        for line in read_content:
            list = line.split(" ")
            if list[0] == "Square":
                side = int(list[5])
                perimeter_square = 4 * side
                area_square = side * side
                result_square = f"{list[0]} Perimeter {perimeter_square} Area {area_square}"
            if list[0] == "Rectangle":
                side_first = int(list[2]) - int(list[5])
                side_second = int(list[3]) - int(list[6])
                perimeter_rectangle = 2 * (side_first + side_second)
                area_rectangle = side_first * side_second
                result_rectangle = f"{list[0]} Perimeter {perimeter_rectangle} Area {area_rectangle}"
            if list[0] == "Circle":
                radius = int(list[5])
                perimeter_circle = 2 * pi * radius
                area_circle = pi * radius * radius
                result_circle = f"{list[0]} Perimeter {math.ceil(perimeter_circle)} Area {math.ceil(area_circle)}"
    with open("output.txt", "w") as file_to_write:
        file_to_write.write(result_square + "\n")
        file_to_write.write(result_rectangle + "\n")
        file_to_write.write(result_circle)


if __name__ == '__main__':
    main()

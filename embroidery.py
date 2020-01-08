def draw_rectangle(width, height, border=0):
    matrix = []
    matrix1 = []
    i = 0
    inside_content = 2
    b = 0
    inside_width = width - border*2
    inside_heigh = height - border*2
    while i != height:
        while b != width:
            matrix.append(1)
            b = b+1
        i = i + 1
        matrix1.append(matrix[:])
    if border > 0:
        for i in range(inside_heigh):
            f = 0
            while f != inside_width:
                matrix1[border+i][border+f] = inside_content
                f = f+1
    return matrix1


def draw_triangle(height):
    matrix = []
    matrix1 = []
    i = 0
    inside_content = 1
    inside_content_2 = 2
    b = 0
    width = (height * 2) - 1
    height1 = height - 1
    while i != height:
        while b != width:
            matrix.append(0)
            b = b+1
        i = i + 1
        matrix1.append(matrix[:])

    counter_for_row = 0
    list_changer = 1
    for counter_for_row in range(height):
        i = 0
        i_2 = 0
        while i != height-counter_for_row:
            matrix1[(height-list_changer)][i+counter_for_row] = inside_content
            i = i + 1
        while i_2 != height-counter_for_row:
            matrix1[(height-list_changer)][height1+i_2] = inside_content
            i_2 = i_2 + 1
        counter_for_row = counter_for_row + 1
        list_changer = list_changer + 1

        f = 0
        g = 1
        while i != width:
            matrix1[(height-g)][i] = inside_content_2
            i = i + 1
        while f != height:
            matrix1[(height-g)][f] = inside_content_2
            matrix1[(height-g)][width-g] = inside_content_2
            f = f + 1
            g = g + 1
        i = i + 1
    return matrix1


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()


if __name__ == '__main__':
    color_scheme = {0: ' ', 1: '*', 2: '|'}
    embroider(draw_rectangle(15, 15, 2), color_scheme)
    embroider(draw_triangle(15), color_scheme)


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


'''
def draw_christmas_tree_2(blocks):
    matrix1 = draw_triangle(4)

    matrix2.append(matrix1)
    matrix2 = matrix1[0:3]
    print(matrix1)

    return matrix2
'''


def draw_christmas_tree(blocks):
    matrix = []
    matrix1 = []
    height = 3
    i = 0
    inside_content = 1
    inside_content_2 = 2
    b = 0
    a = 0
    width = height * blocks - 1

    # Draw matrix with 0
    while a != blocks:
        i = 0
        while i != height:
            while b != width:
                matrix.append(0)
                b = b+1
            i = i + 1
            matrix1.append(matrix[:])
        a = a + 1

    # Draw trinagle
    x = 0
    x_1 = 0
    x_2 = 0
    while x != width+1:
        i_2 = 1
        i_3 = 2
        i = 0
        while i != width-x_2:
            matrix1[width-x][i+x_1] = inside_content
            i = i + 1
        if blocks > 1:
            while i_2 != width-(1+x_2):
                matrix1[width-(1+x)][i_2+x_1] = inside_content
                i_2 = i_2 + 1
        if blocks > 2:
            while i_3 != width-(2+x_2):
                matrix1[width-(2+x)][i_3+x_1] = inside_content
                i_3 = i_3 + 1
        x = x + 3
        x_1 = x_1 + 1
        x_2 = x_2 + 2

    # Draw border

    i = 0
    while i != width:
        matrix1[width][i] = inside_content_2
        i = i + 1
    c = 0
    x_3 = 0
    for c in range(blocks):
        i = 0
        while i != height:
            matrix1[width-(i+x_3)][i+c] = inside_content_2
            matrix1[width-(i+x_3)][-1-(i+c)] = inside_content_2
            i = i + 1
        x_3 = x_3 + 3
        c = c + 1

    return matrix1


def draw_circle(radius):
    matrix = []
    matrix1 = []
    i = 0
    b = 0
    width = (radius*2) + 1
    while i != width:
        while b != width:
            matrix.append(0)
            b = b+1
        i = i + 1
        matrix1.append(matrix[:])

    line_count = 0
    a = 0
    for x in matrix1:
        i = 1
        a = 0
        while a != width:
            k = line_count-radius
            p = a-radius
            if k*k + p*p <= radius*radius:
                matrix1[line_count][a] = 2
            elif k*k + p*p <= (radius+1)*(radius+1):
                matrix1[line_count][a] = 1
            a = a + 1
        i = i + 1
        line_count = line_count + 1
    return(matrix1)


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()


if __name__ == '__main__':
    color_scheme = {0: ' ', 1: '.', 2: '*'}
    embroider(draw_rectangle(15, 15, 2), color_scheme)
    embroider(draw_triangle(20), color_scheme)
    embroider(draw_christmas_tree(4), color_scheme)
    embroider(draw_circle(10), color_scheme)

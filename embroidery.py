def draw_rectangle(width, height, border=0):
    matrix = []
    matrix1 = []
    i = 0
    inside_content = 2
    b = 0
    insert_width = width - border*2
    insert_heigh = height - border*2
    while i != height:
        while b != width:
            matrix.append(1)
            b = b+1
        i = i + 1
        matrix1.append(matrix[:])
    if border > 0:
        for i in range(insert_heigh):
            f = 0
            while f != insert_width:
                matrix1[border+i][border+f] = inside_content
                f = f+1
    return matrix1


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()


if __name__ == '__main__':
    color_scheme = {0: ' ', 1: '*', 2: '.'}
    embroider(draw_rectangle(100, 100, 10), color_scheme)

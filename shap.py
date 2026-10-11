import math
shapes = ['square', 'circle', 'rectangle', 'cylinder', 'sphere', 'square pyramid', 'semicircle', 'trapezium', 'rhombus', 'parallelogram']
for a in shapes:
    print(a)


shape = input('what shape do you wish to wish to calculate: ').lower()
if shape.isalpha():
    shape = str(shape)

    if shape == 'square':
        a = input('do you wish to calculate area or perimeter?  ').lower()
        if a == 'area':
            try:
                l = input('what is the length of the square: ')
                l = float(l)
                Ans = l ** 2
                print(f'the area of the square is: {Ans}')
            except:
                print('wrong input')
        elif a == 'perimeter':
            try:
                l = input('what is the length of the square: ')
                l = float(l)
                A = l + l
                print(f'the perimeter of the square is: {A}')
            except:
                print('wrong input')
        else:
            print('wrong input')


    elif shape == 'circle':
        c = input('circumference or area? ').lower()
        if c == 'area':
            try:
                r = input('what is the radius of the circle: ')
                r = float(r)
                Ans = r ** 2 * math.pi
                print(f'the area of the circle is: {Ans}')
            except:
                print('wrong input')

        elif c == 'circumference':
            try:
                r = input('what is the radius of the circle: ')
                r = float(r)
                Ans = 2 * math.pi * r
                print(f'the circumference of the circle is: {Ans}')
            except:
                print('wrong input')
        else:
            print('wrong input')

    elif shape == 'rectangle':
        rec = input('area or perimeter? ').lower()
        if rec == 'area':
            try:
                l = input('what is the length of the rectangle: ')
                b = input('what is the breath of the rectangle: ')
                l = float(l)
                b = float(b)
                Ans = l * b
                print(f'the area of the rectangle is: {Ans}')
            except:
                print('wrong input')
        elif rec == 'perimeter':
            try:
                l = input('what is the length of the rectangle: ')
                b = input('what is the breath of the rectangle: ')
                l = float(l)
                b = float(b)
                Ans = l + l + b + b
                print(f'the perimeter of the rectangle is: {Ans}')
            except:
                print('wrong input')
        else:
            print('wrong input')

    elif shape == 'cylinder':
        c = input('total surface area or volume? ').lower()
        if c == 'volume':
            try:
                h = input('what is the height of the cylinder: ')
                r = input('what is the radius of the cylinder: ')
                h = float(h)
                r = float(r)
                Ans = h * (r ** 2) * math.pi
                print(f'the volume of the cylinder is: {Ans}')
            except:
                print('wrong input')
        elif c == 'area' or c == 'total surface area':
            try:
                h = input('what is the height of the cylinder: ')
                r = input('what is the radius of the cylinder: ')
                h = float(h)
                r = float(r)
                Ans = (2 * math.pi * r * h) + (2 * math.pi * (r ** 2))
                print(f'the area of the cylinder is: {Ans}')

            except:
                print('wrong input')
        else:
            print('wrong input')

    elif shape == 'sphere':
        s = input('volume or area? ').lower()
        if s == 'volume':
            try:
                h = input('what is the radius of the sphere: ')
                h = float(h)
                ans = (4 / 3) * math.pi * h ** 3
                print(f'the volume of the sphere is: {ans}')
            except:
                print('wrong input')
        elif s == 'area':
            # noinspection PyBroadException
            try:
                h = input('what is the radius of the sphere: ')
                h = float(h)
                ans = 4 * math.pi * h ** 2
                print(f'the area of the sphere is: {ans}')
            except:
                print('wrong input')
        else:
            print('wrong input')

    elif shape == 'semicircle':
        c = input('area or circumference? ').lower()
        if c == 'area':
            try:
                l = input('what is the radius of the semicircle: ')
                l = float(l)
                ans = (1 / 2) * math.pi * l ** 2
                print(f'the area of the semicircle is: {ans}')
            except:
                print('wrong input')
        elif c == 'circumference':
            try:
                l = input('what is the radius of the semicircle: ')
                l = float(l)
                ans = (math.pi * l) + (2 * l)
                print(f'the circumference of the semicircle is: {ans}')
            except:
                print('wrong input')
        else:
            print('wrong input')

    elif shape == 'rhombus':
        h = input('area or perimeter? ').lower()
        if h == 'area':
            try:
                l = input('what is the first diagonal of the rhombus: ')
                j = input('what is the second diagonal of the rhombus: ')
                l = float(l)
                j = float(j)
                hog = (1/2) * l * j
                print(f'the area of the rhombus is: {hog}')
            except:
                print('wrong input')
        elif h == 'perimeter':
            try:
                l = input('what is the side of the rhombus: ')
                l = float(l)
                hog = 4 * l
                print(f'the perimeter of the rhombus is: {hog}')
            except:
                print('wrong input')
        else:
            print('wrong input')

    elif shape == 'parallelogram':
        p = input('area or perimeter? ').lower()
        if p == 'area':
            try:
                l = input('what is the base of the parallelogram: ')
                a = input('what is the height of the parallelogram: ')
                l = float(l)
                a = float(a)
                ans = a * l
                print(f'the area of the parallelogram is: {ans}')
            except:
                print('wrong input')
        elif p == 'perimeter':
            try:
                l = input('what is the first side of the parallelogram: ')
                a = input('what is the second side of the parallelogram: ')
                l = float(l)
                a = float(a)
                ans = 2 * (a + l)
                print(f'the perimeter of the parallelogram is: {ans}')
            except:
                print('wrong input')
        else:
            print('wrong input')
    elif shape == 'trapezium':
        g = input('area or perimeter? ').lower()
        if g == 'area':
            try:
                l = input('what is the height of the trapezium: ')
                f = input('what is the first side of the trapezium: ')
                k = input('what is the second side of the trapezium: ')
                l = float(l)
                f = float(f)
                k = float(k)
                ans = (1/2) * (f + k) * l
                print(f'the area of the trapezium is: {ans}')
            except:
                print('wrong input')
        elif g == 'perimeter':
            try:
                l = input('what is the first side of the rhombus: ')
                j = input('what is the second side of the rhombus: ')
                k = input('what is the third side of the rhombus: ')
                i = input('what is the fourth side of the rhombus: ')
                l = float(l)
                j = float(j)
                k = float(k)
                i = float(i)
                jar = l + i + j + k
                print(f'the perimeter of the  is trapezium: {jar}')
            except:
                print('wrong input')
        else:
            print('wrong input')
    elif shape == 'square pyramid':
        b = input('area or perimeter? ').lower()
        if b == 'area':
            try:
                l = input('what is the slant height of the pyramid: ')
                f = input('what is the length of the pyramid: ')
                l = float(l)
                f = float(f)
                ans = (f**2) + (2 * l *f)
                print(f'the area of the pyramid is: {ans}')
            except:
                print('wrong input')
        elif b == 'perimeter':
            try:
                l = input('what is the length of the pyramid: ')
                l = float(l)
                ans = 4 * l
                print(f'the perimeter of the pyramid is: {ans}')
            except:
                print('wrong input')
        else:
            print('wrong input')
    else:
        print('invalid')
else:
    print('not a word')


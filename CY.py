def vcy():
    simple = input('Что надо найти? (h - высота, r - радиус, v - объём, sc - площадь основания, sb - площадь бока): ')
    pi = float(input('Число пи: '))
    if simple == 'h':
        y_n = input('Объём дробный? (y/n): ')
        if y_n == 'y':
            v = float(input('Объём: '))
        else:
            v = int(input('Объём: '))
        y_n2 = input('Радиус дробный? (y/n): ')
        if y_n2 == 'y':
            r = float(input('Радиус: '))
        else:
            r = int(input('Радиус: '))
        ret1 = str(v / (pi * (r * r))) + ' см.'
        return ret1
    else:
        if simple == 'r':
            y_n = input('Объём дробный? (y/n): ')
            if y_n == 'y':
                v = float(input('Объём: '))
            else:
                v = int(input('Объём: '))
            y_n2 = input('Высота дробная? (y/n): ')
            if y_n2 == 'y':
                h = float(input('Высота: '))
            else:
                h = int(input('Высота: '))
            ret1 = str((v / h) / (pi * 2)) + ' см2.'
            return ret1
        else:
            if simple == 'v':
                y_n = input('Радиус дробный? (y/n): ')
                if y_n == 'y':
                    r = float(input('Радиус: '))
                else:
                    r = int(input('Радиус: '))
                y_n2 = input('Высота дробная? (y/n): ')
                if y_n2 == 'y':
                    h = float(input('Высота: '))
                else:
                    h = int(input('Высота: '))
                ret1 = str(pi * (r * r) * h) + ' см3.'
                return ret1
            else:
                if simple == 'sc':
                    y_n = input('Радиус дробный? (y/n): ')
                    if y_n == 'y':
                        r = float(input('Радиус: '))
                    else:
                        r = int(input('Радиус: '))
                    ret1 = str(pi * (r * r)) + ' см2.'
                    return ret1
                else:
                    if simple == 'sb':
                        y_n = input('Радиус дробный? (y/n): ')
                        if y_n == 'y':
                            r = float(input('Радиус: '))
                        else:
                            r = int(input('Радиус: '))
                        y_n2 = input('Высота дробная? (y/n): ')
                        if y_n2 == 'y':
                            h = float(input('Высота: '))
                        else:
                            h = int(input('Высота: '))
                        ret1 = str(pi * (r * r) * h) + ' см2.'
                        return ret1
                    else:
                        return 'error'

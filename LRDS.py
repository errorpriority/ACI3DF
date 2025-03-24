def lrds():
  simple = input('Что надо найти? (l - длина окружности, r - радиус, d - диаметр, s - площадь): ')
  pi = float(input('Число пи: '))
  if simple == 'l':
      y_n = input('Диаметр дробный? (y/n): ')
      if y_n == 'y':
          d = float(input('Диаметр: '))
      else:
          d = int(input('Диаметр: '))
      ret1 = str(pi * d) + ' см.'
      return ret1
  else:
      if simple == 'r':
          y_n = input('Длина окружности дробная? (y/n): ')
          if y_n == 'y':
              l = float(input('Длина окружности: '))
          else:
              l = int(input('Длина окружности: '))
          ret1 = str(l / (pi * 2)) + ' см.'
          return ret1
      else:
          if simple == 'd':
              y_n = input('Длина окружности дробная? (y/n): ')
              if y_n == 'y':
                l = float(input('Длина окружности: '))
              else:
                l = int(input('Длина окружности: '))
              ret1 = str(l / pi) + ' см.'
              return ret1
          else:
              if simple == 's':
                  y_n = input('Радиус дробный? (y/n): ')
                  if y_n == 'y':
                      r = float(input('Радиус: '))
                  else:
                      r = int(input('Радиус: '))
                  ret1 = str(pi * (r * r)) + ' см2.'
                  return ret1
              else:
                return 'error'

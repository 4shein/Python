"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""

class Road():
    _width = None
    _length = None
    _thickness = None
    _density = None


    def weight(self, _length, _width, _thickness, _density):
        self._length = _length
        self._width = _width
        self._thickness = _thickness
        self._density = _density
        return _length * _width * _density * _thickness

m4 = Road()

print(m4.weight(20, 5000, 25, 5))


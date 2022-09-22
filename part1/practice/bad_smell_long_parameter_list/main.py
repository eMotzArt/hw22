# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

from enum import Enum, unique
@unique
class States(Enum):
    # State = speed modifier
    STAND = 1
    CROUCH = 0.5
    FLY = 1.2


class Unit:

    def __init__(self, start_x: int, start_y: int, field: str, speed: int = 1):
        self.speed = speed
        self.field = field
        self.x = start_x
        self.y = start_y
        self.state: States = States.STAND

    def set_crouch(self):
        """Переводит персонажа в положение приседа"""
        self.state = States.CROUCH
        print('Персонаж присел')

    def set_fly(self):
        """Переводит персонажа в положение полета"""
        self.state = States.FLY
        print('Персонаж взлетел')

    def set_standing(self):
        """Переводит персонажа в положение стоя"""
        if self.state == States.FLY:
            print('Персонаж приземлился и встал')
        else:
            print('Персонаж встал')
        self.state = States.STAND

    def _get_speed(self):
        """Возвращает текущую скорость движения"""
        return self.speed * self.state.value

    def _print_movement(self):
        print(f"Персонаж сделал ход. Новые координаты: X = {self.x}. Y = {self.y}")

    def move(self, direction):
        """Перемещает персонажа"""
        current_speed = self._get_speed()
        if direction == 'UP':
            self.y += current_speed
        elif direction == 'DOWN':
            self.y -= current_speed
        elif direction == 'LEFT':
            self.x -= current_speed
        elif direction == 'RIGHT':
            self.x += current_speed
        self._print_movement()



u = Unit(1,1,'Some battle field')
u.move('RIGHT')
u.move('UP')
u.set_crouch()
u.move('LEFT')
u.move('UP')
u.set_fly()
u.move('DOWN')
u.set_standing()
u.move('UP')

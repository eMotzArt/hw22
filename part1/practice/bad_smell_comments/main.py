# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев

#MY_SOLUTION

class Unit:
    def move(self, field, x, y, direction, is_flying, is_crouch, speed = 1):
        """Функция реализует перемещение юнита по полю.
        :param field: поле по которому перемещается юнит
        :param x: x-координата юнита
        :param y: у- координата юнита
        :param direction: направление перемещения
        :param is_flying: летит ли юнит
        :param is_crouch: крадется ли юнит
        :param speed: базовый параметр скорости
        """
        if is_flying and is_crouch:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_flying:
            speed *= 1.2
            if direction == 'UP':
                new_y = y + speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + speed
        if is_crouch:
            speed *= 0.5
            if direction == 'UP':
                new_y = y + speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)


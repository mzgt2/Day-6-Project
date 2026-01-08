def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def vertical():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left


def seek_wall():
    while front_is_clear() and right_is_clear():
        move()


def seek_wall2():
    if wall_in_front() and right_is_clear():
        turn_around()


seek_wall()
seek_wall2()
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif not front_is_clear() and wall_on_right():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()

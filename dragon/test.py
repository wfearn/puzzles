import dragon_state

def case_one():
    c = dragon_state.GameInstance(11, 5, 16, 5, 0, 0)
    assert(c.min_turns() == 5)

def case_two():
    c = dragon_state.gameInstance(3, 1, 3, 2, 2, 0)
    assert(c.min_turns() == 2)

def case_three():
    c = dragon_state.GameInstance(3, 1, 3, 2, 1, 0)
    assert(c.min_turns() == None)

if __name__ == '__main__':
    case_one()
    case_two()
    case_three()

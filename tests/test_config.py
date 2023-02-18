class NotInRange(Exception):
    def __init__(self, message="value_not_range"):

        #self.input_ = input_
        self.message = message
        super().__init__(self.message)

def test_generic():
    a=2
    b=2

    if a not in range(10,20):
        raise NotInRange
    else:
        pass
    assert a != b

test_generic()
from hype import *


def test_element():

    class Test(Element):
        tag='test'

    test = Test(4)
    assert str(test) == '\ntest'


def test_div():
    div = Div(4)
    assert str(div) == '\n<div>4</div>'


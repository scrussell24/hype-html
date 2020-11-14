from hype import *


def test_doc():
    assert str(Doc()) == '<!DOCTYPE html>'


def test_doc_nested():
    assert str(Doc(Html())) == '<!DOCTYPE html>\n<html></html>'


def test_custom_element():
    class Test(Element):
        tag='test'
    assert str(Test(4)) == '\n<test>4</test>'


def test_generated_element():
    assert str(Div(4)) == '\n<div>4</div>'


def test_nested_elements():
    assert str(Div(H1('Hello World'))) == '\n<div>\n  <h1>Hello World</h1>\n</div>'


def test_attribute():
    assert str(Div('test', width=10)) == '\n<div width="10">test</div>'


def test_multiple_attributes():
    assert str(Div('test', width=10, height="20")) == '\n<div width="10" height="20">test</div>'


def test_underscore_attributes():
    assert str(Div('test', _id="hi")) == '\n<div id="hi">test</div>'


def test_underscore_attributes():
    assert str(Div('test', test_attr="hi")) == '\n<div test-attr="hi">test</div>'


def test_self_closing_tag():
    assert str(Hr()) == '\n<hr/>'

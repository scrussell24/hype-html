import pytest

from hype.asyncio import *


@pytest.mark.asyncio
async def test_doc():
    assert await Doc().render() == "<!DOCTYPE html>"


@pytest.mark.asyncio
async def test_doc_nested():
    assert await Doc(Html()).render() == "<!DOCTYPE html>\n<html></html>"


@pytest.mark.asyncio
async def test_custom_element():
    class Test(Element):
        tag = "test"

    assert await Test(4).render() == "\n<test>4</test>"


@pytest.mark.asyncio
async def test_generated_element():
    assert await Div(4).render() == "\n<div>4</div>"


@pytest.mark.asyncio
async def test_nested_elements():
    assert (
        await Div(H1("Hello World")).render()
        == "\n<div>\n  <h1>Hello World</h1>\n</div>"
    )


@pytest.mark.asyncio
async def test_attribute():
    assert await Div("test", width=10).render() == '\n<div width="10">test</div>'


@pytest.mark.asyncio
async def test_multiple_attributes():
    assert (
        await Div("test", width=10, height="20").render()
        == '\n<div width="10" height="20">test</div>'
    )


@pytest.mark.asyncio
async def test_underscore_attributes():
    assert await Div("test", _id="hi").render() == '\n<div id="hi">test</div>'


@pytest.mark.asyncio
async def test_underscore_attributes():
    assert (
        await Div("test", test_attr="hi").render() == '\n<div test-attr="hi">test</div>'
    )


@pytest.mark.asyncio
async def test_self_closing_tag():
    assert await Hr().render() == "\n<hr/>"


@pytest.mark.asyncio
async def test_self_closing_tag_discard_inner_elements():
    assert await Hr("test").render() == "\n<hr/>"


@pytest.mark.asyncio
async def test_custom_self_closing_tag():
    class Test(SelfClosingElement):
        tag = "test"

    assert await Test().render() == "\n<test/>"


@pytest.mark.asyncio
async def test_other_indent():
    assert (
        await Div(H1("Hello World")).render(indent=Indent.TAB)
        == "\n<div>\n\t<h1>Hello World</h1>\n</div>"
    )
    assert (
        await Doc(Div(H1("Hello World")), indent=Indent.TAB).render()
        == "<!DOCTYPE html>\n<div>\n\t<h1>Hello World</h1>\n</div>"
    )


@pytest.mark.asyncio
async def test_boolean_attribute_false():
    div = Div("content", test=False)
    assert await div.render() == "\n<div>content</div>"


@pytest.mark.asyncio
async def test_boolean_attribute_true():
    div = Div("content", test=True)
    assert await div.render() == "\n<div test>content</div>"


@pytest.mark.asyncio
async def test_add_element():
    div = Div("content")
    div.append(P("test"))
    assert await div.render() == "\n<div>content\n  <p>test</p>\n</div>"


@pytest.mark.asyncio
async def test_add_attribute():
    div = Div("content")
    div.attrs(test="test")
    assert await div.render() == '\n<div test="test">content</div>'

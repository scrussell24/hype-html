# hype

A minimal python dsl for generating html.

## Install

Install via pip

```
pip install hype-html
```

Alteratively, in the spirit of removing dependencies, you could simply copy/paste the hype/element.py file into your project.

## Usage

Hype exposes classes for each html tag.

```
from hype import *

doc = Doc(Html('Hello World!'))

print(doc)

# <!DOCTYPE html>
# <div>Hello World!</div>
```

Elements can also be rendered by calling.

```
doc() == str(doc)
```
### Inner HTML

Arguments passed in the element constructor are rendered using the str function and indented (if the element only has one argument it will not be indented.)

```
body = Body(
    H1('Hello World'),
    P('This is a paragraph'),
    'Just a string',
    P('Another paragraph')
)

print(body)

# <body>
#   <h1>Hello World</h1>
#   <p>This is a paragraph</p>Just a string
#   <p>Another paragraph</p>
# </body>
```

### Attributes

Attributes are passed as keyword arguments to the element's constructor.

```
span = Span('span', width='50px')

print(span)

# <span width="50px">span</span>
```

Since some built-in, and possibly custom, attributes conflict with python keywords, keywords will automatically have all leading underscores stripped.

```
span = Span('span', _id='my-span', width='50px')

print(span)

# <span id="my-span" width="50px">span</span>

```
Any remaining underscores will be converted to hyphens.

```
span = Span('span', custom_attrbiute='custom')

print(span)

# <span custom-attribute="custom">span</span>
```

### Custom Elements

If you to create a custom tag, just subtype the Element class and add a tag.

```
class CustomTag(Element):
    tag = 'custom-tag'

tag = CustomTag()
print(tag)

# <custom-tag></custom-tag>
```
To create a custom self closing tag, subtype the SelfClosingElement class.

```
class CustomTag(SelfClosingElement):
    tag = 'custom-tag'

tag = CustomTag()
print(tag)

# <custom-tag/>
```

### Indents

The indent to be used can be passed as a keyword arg to the Doc constructor.

```
doc = Doc(content, indent=Indent.TAB)
```

It can also be passed as a keyword arg when calling and element.

```
div = Div(H1('Header'))
print(div(indent=Indent.FOUR_SPACES))

# <div>
#    <h1>Header</h1>
# </div>
```

<!-- ## Development

### Install

### Pre Processor

### Tests -->
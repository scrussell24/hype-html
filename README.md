# hype

A minimal python dsl for generating html.

## Install

```
pip install hype
```

## Usage

Hype ships with classes for each html tag as well as a few other helpful classes.

```
from hype import *

doc = Doc(
    Html(
        Body(
            H1('Hello'),
            P('World')
        )
    )
)

print(doc)
```
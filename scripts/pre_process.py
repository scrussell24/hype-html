import json

from jinja2 import Template


def generate():
    with open("tags.json", "r") as f:
        tags = json.loads(f.read())

    with open("templates/element.py.j2", "r") as f:
        template = f.read()
    tmp = Template(template)
    code = tmp.render(tags=tags)
    with open("hype/element.py", "w") as f:
        f.write(code)

    with open("templates/__init__.py.j2", "r") as f:
        template = f.read()
    tmp = Template(template)
    code = tmp.render(tags=tags)
    with open("hype/__init__.py", "w") as f:
        f.write(code)


if __name__ == "__main__":
    generate()

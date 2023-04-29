import sys
import json


def add_attribute(attr, *matched_tags):
    with open("tags.json", "r") as f:
        tags = json.loads(f.read())

    for tag, data in tags.items():
        if tag in matched_tags:
            data.get("attrs").append(attr)
        if len(matched_tags) == 1 and matched_tags[0] == "global":
            data.get("attrs").append(attr)

    with open("tags.json", "w") as f:
        f.write(json.dumps(tags, indent=2))


if __name__ == "__main__":
    add_attribute(sys.argv[1], *sys.argv[2:])

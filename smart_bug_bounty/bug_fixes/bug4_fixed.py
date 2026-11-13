"""Exercise: independent calls should create independent tag lists."""


def add_tag(tag, tags=None):
    """Append to a supplied list or create a fresh list when omitted."""
    if not isinstance(tag, str) or not tag.strip():
        raise ValueError("tag must be a non-empty string")
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


if __name__ == "__main__":
    first = add_tag("security")
    second = add_tag("performance")
    print("First:", first)
    print("Second:", second)

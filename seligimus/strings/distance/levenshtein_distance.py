"""The Levenshtein distance between two strings."""


def levenshtein_distance(string_a: str, string_b: str) -> int:
    """Return the Levenshtein distance between two strings."""
    if not string_a or not string_b:
        return 0

    head_a, tail_a = string_a[0], string_a[1:]
    head_b, tail_b = string_b[0], string_b[1:]

    if head_a == head_b:
        return levenshtein_distance(tail_a, tail_b)

    return 1 + min(levenshtein_distance(tail_a, string_b), levenshtein_distance(string_a, tail_b),
                   levenshtein_distance(tail_a, tail_b))

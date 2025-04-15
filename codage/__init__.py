def isPrefix(u, v):
    """
    Détermine si u est un préfixe de v
    Params:
        - u : le mot à tester comme préfixe
        - v : le mot sur lequel on teste le préfixe
    Returns:
        - (-1) si ce n'est pas un préfixe
        - (0) si u == v
        - (1) si u est un vrai préfixe de v
    """
    if v.startswith(u):
        if u == v:
            return 0
        else:
            return 1
    return -1
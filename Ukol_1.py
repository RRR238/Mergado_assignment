def brute_force(pool, last=None, so_far=None):
    so_far = so_far or []
    if not pool:
        return so_far
    candidates = []
    for w in pool:
        if not last or w.startswith(last):
            c_so_far, c_pool = list(so_far) + [w], set(pool) - set([w])
            candidates.append(brute_force(c_pool, w[-1], c_so_far))
    return max(candidates, key=len, default=so_far)






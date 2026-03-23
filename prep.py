#The goal is to test every possible return path.
# we have 6 possible behaviors, so we need 6 tests. 
def strange_function(a, b, c, d):
    if a == b:
        if c < d:
            return 'behaviour 1'
        else:
            return 'behaviour 2'
    elif a < c:
        return 'behaviour 3'
    else:
        if d < b:
            return 'behaviour 4'
        elif c < a:
            return 'behaviour 5'
        else:
            return 'behaviour 6'
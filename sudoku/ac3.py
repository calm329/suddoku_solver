from sudoku.backtracking import is_consistent

def create_arcs(csp):
    arcs = []
    for (Xi, Xj) in csp.constraints:
        arcs.append((Xi, Xj))
    return arcs

def revise(csp, Xi, Xj):
    revised = False
    for x in csp.domain[Xi][:]:  # Iterate over a copy of Xi's domain
        # Check if there's a value in Xj's domain that satisfies the constraint with Xi
        if not any(is_consistent(Xi, x, {Xi: x, Xj: y}, csp) for y in csp.domain[Xj]):
            csp.domain[Xi].remove(x)
            revised = True
    return revised

def ac3(csp):
    queue = create_arcs(csp)
    while queue:
        (Xi, Xj) = queue.pop(0)
        if revise(csp, Xi, Xj):
            if not csp.domain[Xi]:  # If domain is empty after revision, return failure
                return False
            # Add neighbors of Xi back into the queue
            for Xk, Xl in csp.constraints:
                if Xk == Xi and Xl != Xj:
                    queue.append((Xl, Xi))
    return True

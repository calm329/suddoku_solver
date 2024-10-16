def backtrack(assignments, csp):
    if len(assignments) == 81:  # Puzzle solved when all 81 cells are assigned
        return True, assignments

    var = select_unassigned_variable(assignments, csp)
    for value in csp.domain[var]:
        if is_consistent(var, value, assignments, csp):
            assignments[var] = value
            result, new_assignments = backtrack(assignments, csp)
            if result:
                return True, new_assignments
            del assignments[var]  # Backtrack if the assignment doesn't work
    return False, assignments

def select_unassigned_variable(assignments, csp):
    # Use MRV heuristic: choose the variable with the smallest remaining domain
    return min([v for v in csp.domain if v not in assignments], key=lambda var: len(csp.domain[var]))

def is_consistent(var, value, assignments, csp):
    # Check if assigning `value` to `var` breaks any constraints
    for neighbor in [n for (x, n) in csp.constraints if x == var]:
        if neighbor in assignments and assignments[neighbor] == value:
            return False
    return True

import string


ALPHABET = string.ascii_uppercase


def read_input_file(f):
    with open(f, 'r') as input:
        return input.read().strip().split('\n')


def _parse_step(step):
    parts = step.split(" ")
    return (parts[1], parts[7])


def find_order(steps):
    # Maps step to a set of its prerequisites
    step_dependencies = _group_dependencies(steps)
    
    order = ""

    while step_dependencies:
        next_step = _find_next_step(step_dependencies)
        order += next_step
        step_dependencies = _complete_step(next_step, step_dependencies)
    
    return order


def task_duration(step_rules, base_step_duration, num_workers):
    # We will treat the workers list as a stack to provide workers
    # when they are available
    workers = [1] * num_workers
    
    elapsed = 0
    active_steps = {}  # Map step being worked on to remaining minutes of work

    step_dependencies = _group_dependencies(step_rules)
    
    while step_dependencies:
        
        # Schedule some work
        while True:
            next_step = _find_next_step(step_dependencies)
        
            if not next_step or not workers:
                break
            
            # Take a worker and activate the step
            workers.pop()
            active_steps[next_step] = _step_duration(next_step, base_step_duration)
        
        completed_steps = [s for s, v in active_steps.iteritems() if v == 0]
        for step in completed_steps:
            step_dependencies = _complete_step(step, step_dependencies)
            del active_steps[step]
            # Worker is freed up, add back to stack
            workers.append(1)


        # Log it out bitch
        print "Second: " + str(elapsed) + " " + " ".join(s for s in active_steps)

        for step in active_steps:
            active_steps[step] -= 1

        completed_steps = [s for s, v in active_steps.iteritems() if v == 0]

        elapsed += 1


    return elapsed


def _step_duration(step, base_duration):
    for i, letter in enumerate(ALPHABET):
        if step == letter:
            return base_duration + i + 1

    raise Exception("No step duration found for step " + step)


def _complete_step(step, step_dependencies):
    # This step is complete, remove it from the list of remaining steps
    del(step_dependencies[step])
    # Remove this step from the prereqs of the other steps b/c it is now complete
    step_dependencies = _mark_step_complete(step, step_dependencies)

    return step_dependencies


def _find_next_step(step_dependencies):
    steps_without_prereq = _find_steps_without_prereq(step_dependencies)
    return _break_step_tie(steps_without_prereq)


def _find_steps_without_prereq(step_dependencies):
    return [step for step, prereq in step_dependencies.iteritems() if not prereq]


def _break_step_tie(steps):
    return sorted(steps)[0]


def _mark_step_complete(step, dependencies):
    for prereqs in dependencies.values():
        if step in prereqs:
            prereqs.remove(step)
    return dependencies


def _group_dependencies(steps):
    dependencies = {}
    for step in steps:
        prereq, step = _parse_step(step)
        
        if step not in dependencies:
            dependencies[step] = set()
        if prereq not in dependencies:
            dependencies[prereq] = set()

        dependencies[step].add(prereq)
    
    return dependencies


if __name__ == "__main__":
    import sys
    f = sys.argv[1]

    steps = read_input_file(f)

    print "Order:", find_order(steps)


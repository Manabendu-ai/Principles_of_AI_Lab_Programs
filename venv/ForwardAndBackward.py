facts = {"fever", "cough"}

rules = [
    ({"fever", "cough"}, "flu"),
    ({"flu"}, "take_medicine")
]

def forward_chaining(facts, rules):
    new_fact = True

    while new_fact:
        new_fact = False
        for condition, result in rules:
            if condition.issubset(facts) and result not in facts:
                facts.add(result)
                new_fact = True

    return facts

print("Final facts:", forward_chaining(facts, rules))

def backward_chaining(goal, facts, rules):
    if goal in facts:
        return True

    if goal not in rules:
        return False

    for subgoal in rules[goal]:
        if not backward_chaining(subgoal, facts, rules):
            return False

    return True

goal = "take_medicine"

print("Can we prove", goal, "?", backward_chaining(goal, facts, rules))

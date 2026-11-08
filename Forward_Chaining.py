def forward_chaining(facts, rules):
    facts = set(facts)
    changed = True

    while changed:
        changed = False

        for conditions, conclusion in rules:
            if conditions.issubset(facts):
                if conclusion not in facts:
                    facts.add(conclusion)
                    print("New fact derived:", conclusion)
                    changed = True

    return facts


facts = {"rain"}

rules = [
    ({"rain"}, "ground_wet"),
    ({"ground_wet"}, "ground_slippery"),
    ({"ground_slippery"}, "accident_risk")
]

result = forward_chaining(facts, rules)

print("\nFinal facts:")
for fact in sorted(result):
    print(fact)
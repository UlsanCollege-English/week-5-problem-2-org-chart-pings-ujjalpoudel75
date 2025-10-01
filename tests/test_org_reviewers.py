from src.org_reviewers import count_senior

# helpers
def mk(name, level, reports=None):
    return {"name": name, "level": level, "reports": reports or []}

# ---- Normal (4) ----
def test_single_person_meets():
    root = mk("A", 5)
    assert count_senior(root, 4) == 1

def test_single_person_does_not_meet():
    root = mk("A", 2)
    assert count_senior(root, 3) == 0

def test_two_level_tree_mixed():
    root = mk("A", 4, [mk("B", 3), mk("C", 5)])
    assert count_senior(root, 4) == 2

def test_three_level_varied():
    root = mk("A", 3, [
        mk("B", 2, [mk("D", 4)]),
        mk("C", 5)
    ])
    assert count_senior(root, 3) == 3

# ---- Edge (3) ----
def test_none_root():
    assert count_senior(None, 1) == 0

def test_missing_reports_key():
    root = {"name":"A","level":4}   # no reports
    assert count_senior(root, 4) == 1

def test_min_level_high():
    root = mk("A", 5, [mk("B", 5), mk("C", 5)])
    assert count_senior(root, 7) == 0

# ---- Complex (3) ----
def test_wide_tree():
    root = mk("CEO", 6, [mk(f"E{i}", i%7) for i in range(50)])
    assert count_senior(root, 4) == (1 + sum(1 for i in range(50) if i%7 >= 4))

def test_deep_chain():
    node = mk("N0", 1)
    for i in range(1, 60):
        node = mk(f"N{i}", (i%7), [node])
    assert count_senior(node, 5) == sum(1 for i in range(1, 60) if (i%7) >= 5)

def test_mixed_large():
    root = mk("A", 3, [mk("B", 4, [mk("D", 2), mk("E", 6)]), mk("C", 1)])
    assert count_senior(root, 2) == 4

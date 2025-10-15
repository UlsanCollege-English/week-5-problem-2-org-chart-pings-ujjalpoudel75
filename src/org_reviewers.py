# src/org_reviewers.py

def count_senior(root, min_level):
    """
    Return how many people in the org tree have level >= min_level.
    Node format: {"name": str, "level": int, "reports": [nodes]}
    """
    # Handle None input
    if root is None:
        return 0

    # Get current node's level
    level = root.get("level", 0)
    reports = root.get("reports", [])

    # Count current node if meets threshold
    count = 1 if level >= min_level else 0

    # Recurse for each report
    for r in reports:
        count += count_senior(r, min_level)

    return count

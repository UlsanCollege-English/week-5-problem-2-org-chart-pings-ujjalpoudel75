# Org Chart Pings — Who Can Review This PR?

## Story
You’re triaging a critical PR and need a code reviewer with enough seniority. Your company org chart is a tree: each person may have `reports`. You want to quickly **count** how many potential reviewers meet or exceed a target level.

## Technical Description
Write a recursive function:

```py
count_senior(root, min_level) -> int
```

Each node:

```py

{
  "name": "Aisha",
  "level": 3,          # 1 (junior) .. 7 (principal)
  "reports": [ ... ]   # list of nodes
}
```
Return the number of people in the tree with level >= min_level.

## Hints
- Base case: None → 0.

- Self contribution: 1 if level >= min_level else 0.

- Recurse over reports.

## Run Tests Locally
```bash
python -m pytest -q
```
## Common Problems
- Forgetting to include the root in the count.

- Treating missing reports as an error: default to [].

- Using global state; keep it pure per call.
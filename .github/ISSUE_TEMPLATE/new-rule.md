---
name: New Rule
about: Suggest a new rule idea for this project
title: 'New Rule: {Rule Name}'
labels: new rule
assignees: ''

---

**Rule Name:** {NewRuleName}

**Rule Description:**
*{A clear and concise description of new rule}*

**Rule Usage Example:**
```python
reqs = {"data" : "..."}
rule = {"data" : "{new_rule}:{arg1},{arg2}..."}
validate(reqs, rule) # True

reqs = {"data" : "..."}
rule = {"data" : "{new_rule}:{arg1},{arg2}..."}
validate(reqs, rule) # False, It fails because...
```
----------------------------------------------------
**Before contributing please review [RULES.md](https://github.com/CSenshi/Validator/blob/master/RULES.md) (check for duplication), also check [CONTRIBUTING.md](https://github.com/CSenshi/Validator/blob/master/CONTRIBUTING.md) for more details :100:**

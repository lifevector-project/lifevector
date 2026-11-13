# Contributing to PROJECT_NAME

This document describes how the maintainers of PROJECT_NAME work together.
It is a binding agreement between both members and is versioned like code.

## 1. Principles

### 1.1 Equal Contribution
Both members contribute equally to the design, implementation, testing,
and documentation of the project.

### 1.2 Win/Win or No Deal
All decisions follow the **Win/Win or No Deal** paradigm. A decision becomes
part of the project only if both members have benefited from it and are
willing to commit to it. If the members do not agree, the proposal shall not
become part of the project until both agree. Neither member may override the
other, and silence is not agreement.

### 1.3 Equal Ownership
The repository belongs to no single person. It is owned by a GitHub
organization of which both members are owners with equal rights.

## 2. Decision Making

* A proposal is accepted when both members explicitly approve it.
* Changes to the specification (`docs/SPEC.md`) follow the same process as
  changes to code.

## 3. Workflow

### 3.1 Protected Main Branch
No one shall push directly to the `main` branch. This rule applies to both
members equally and is enforced through GitHub branch protection.

### 3.2 Feature Branches
Every change is developed on its own branch, created from an up-to-date
`main`. Branch names shall describe the work, for example:

* `feature/roles-crud`
* `fix/week-range-bug`
* `docs/spec-activities`

### 3.3 Pull Requests
When the work is complete, the author opens a Pull Request into `main`.
The description shall explain what changed and why.

### 3.4 Review and Merge
* The other member reviews the Pull Request.
* The Pull Request is merged only after the reviewer approves it.
* A member shall never approve or merge their own Pull Request.
* If the reviewer requests changes, the author addresses them and requests
  another review.

## 4. Amendments
This document may be changed only through a Pull Request approved by both
members, in accordance with Section 1.2.
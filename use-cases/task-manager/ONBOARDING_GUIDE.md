# Onboarding Guide: 7 Strategies for Approaching Unfamiliar Code

## Introduction

When joining a new team or project, you'll often face a codebase you've never seen. This guide provides battle-tested strategies to get productive quickly without drowning in complexity.

**Expected outcome:** Navigate any unfamiliar codebase confidently in 2-3 days

---

## Strategy 1: Establish Geography First

**Time: 15 minutes | Impact: Saves 2+ hours of confusion**

### Goal
Create a mental map before diving into code details.

### Steps

1. **Create a file inventory**
   ```
   models.py         → Domain entities (Task, TaskStatus, TaskPriority)
   storage.py        → Data persistence layer (JSON file, in-memory dict)
   app.py            → Service/business logic (TaskManager orchestrator)
   cli.py            → User interface (command parsing, output formatting)
   export.py         → Feature module (CSV serialization)
   ```

2. **Identify entry points**
   - Where does execution start? `cli.py` main()
   - How does user input reach code? argparse in cli.py
   - Where does data persist? storage.py saves to tasks.json

3. **Trace one complete flow**
   - Example: `python cli.py create "Test Task"`
   - Flow: cli.py parses args → app.py creates task → storage.py saves → output message
   - Document: "User request → Service logic → Persistence → Response"

4. **Identify the architecture pattern**
   - Layered? (Models → Storage → Service → CLI) ✓
   - MVC? (Model View Controller)
   - Microservices? (independent services)
   - This guides where new code belongs

5. **List key abstractions**
   - What is a Task? (UUID + title + metadata)
   - What is TaskStatus? (finite state: TODO → IN_PROGRESS → REVIEW → DONE)
   - What is priority?  (urgency signal: 1-4)

### Success Criteria
- [ ] I can list all files with one-sentence descriptions
- [ ] I can trace one complete user request through the codebase
- [ ] I can explain the overall architecture pattern
- [ ] I know where new code should go

---

## Strategy 2: Read Tests First (If They Exist)

**Time: 20-30 minutes | Impact: Understand correct usage**

### Goal
Use tests as documentation to understand how code is supposed to work.

### Steps

1. **Find the test structure**
   ```
   tests/
     test_models.py       → How Task objects work
     test_storage.py      → How persistence layer works
     test_app.py          → How service layer works
     test_integration.py  → How layers interact
   ```

2. **For each test file, read test names**
   - `test_task_creation_sets_id()` → "Task should have auto-generated ID"
   - `test_overdue_false_for_completed_task()` → "Business rule: completed tasks aren't overdue"
   - `test_csv_export_escapes_quotes()` → "Edge case: quote handling in export"

3. **Read one failing test**
   - Tells you exact expected behavior
   - Shows what input produces what output
   - Clarifies edge cases

4. **If no tests exist**
   - Write an exploratory test yourself (great learning!)
   - Example: `test_can_create_task_with_all_fields()`
   - Forces you to think: "What are all the ways to create a task?"

### Success Criteria
- [ ] I understand what each module is supposed to do
- [ ] I know the edge cases the team cares about
- [ ] I have concrete examples of correct usage

---

## Strategy 3: Search for Patterns Before Implementing

**Time: 30 minutes | Impact: 70% faster implementation**

### Goal
Reuse existing code patterns instead of from-scratch design.

### Steps

1. **Search for similar functionality**
   ```bash
   # How is data serialized?
   grep -r "JSONEncoder" .
   
   # How are tasks filtered?
   grep -r "get_tasks" .
   
   # How is error handling done?
   grep -r "try:" . | head -5
   
   # How are CLI commands structured?
   grep -r "add_parser" .
   ```

2. **Find the canonical implementation**
   - Best practice: always do it the way it's already done
   - Example: "How do we format task output for display?"
   - Answer: Look at existing `format_task()` function

3. **Copy/adapt instead of create**
   - Copy structure from similar code
   - Modify details for your use case
   - Test that your version works same way

4. **Document why you're following the pattern**
   - Code comment: `# Following pattern from storage.py.get_tasks()`
   - Helps future readers understand decisions

### Example: Adding CSV Export
```python
# Look at how JSON export works (TaskEncoder)
# Adopt same pattern: custom class that transforms objects
# Result: TaskCSVExporter (modeled on TaskEncoder)
# Implementation time: 30 min instead of 2 hours
```

### Success Criteria
- [ ] I found existing similar implementations
- [ ] I understand the architectural pattern
- [ ] My code follows established conventions
- [ ] I documented why I chose this pattern

---

## Strategy 4: Ask Clarifying Questions Before Coding

**Time: 30 minutes | Impact: Prevents rework**

### Goal
Understand ambiguous requirements before implementation.

### Template Questions
```
1. Edge Cases:
   - "What should happen if [unusual scenario]?"
   - "Are there cases where this should NOT apply?"

2. Scope:
   - "Should this affect existing data or only new data?"
   - "Should users be able to undo this action?"

3. Integration:
   - "How will this interact with feature X?"
   - "Should this update statistics/exports?"

4. Configuration:
   - "Is this hardcoded or configurable?"
   - "Should users be able to customize behavior?"

5. Approval:
   - "How do we know this is working correctly?"
   - "What would a failed implementation look like?"
```

### Real Example: Task Abandonment Rule
Questions asked BEFORE coding:
1. Edge case: "What about IN_PROGRESS tasks 7+ days overdue? Abandon them?"
2. Scope: "Should URGENT tasks also be protected from abandonment?"
3. Integration: "Does abandonment trigger notifications?"
4. Configuration: "Is 7 days hardcoded forever or user-configurable?"
5. Approval: "How do we test this works?"

**Result:** Clear requirements → first implementation was correct → no rework

### Success Criteria
- [ ] I asked at least 3 clarifying questions
- [ ] I got written answers (email/Slack/docs)
- [ ] Ambiguities are resolved before coding
- [ ] I documented assumptions in code

---

## Strategy 5: Implement in Layers, Test After Each

**Time: 2-4 hours (with testing) | Impact: Easier debugging**

### Goal
Isolate problems and verify functionality at each architectural layer.

### Layer-by-Layer Approach

**Layer 1: Domain Model**
```python
# models.py: Add new entity or method
class Task:
    def new_method(self):
        # Business logic here
        pass

# Test: Does the method produce correct output?
# python -c "t = Task(...); print(t.new_method())"
```

**Layer 2: Persistence**
```python
# storage.py: Add data access method
def get_modified_tasks():
    # Query logic here
    pass

# Test: Can I retrieve data correctly?
# Does data survive save/load cycle?
```

**Layer 3: Service Logic**
```python
# app.py: Add orchestrator method
def process_modified_tasks(self):
    tasks = self.storage.get_modified_tasks()
    # Business orchestration
    return result

# Test: Does orchestration work?
# Do all layers work together?
```

**Layer 4: User Interface**
```python
# cli.py: Add command
# Result: User can see it working end-to-end

# Test: Does UI display correctly?
# Can user interact as intended?
```

### Why This Works
- **Layer 1 fails**: Problem is in domain logic (easy to fix)
- **Layer 2 fails**: Problem is in queries/persistence (still isolated)
- **Layer 3 fails**: Problem is in orchestration (clear scope)
- **Layer 4 fails**: Problem is in UI/formatting (cosmetic, easy)

**Without this approach:** Bug exists somewhere in 1000+ lines of interconnected code

### Success Criteria
- [ ] I verify domain logic works in isolation
- [ ] I verify persistence layer works in isolation
- [ ] I verify service layer works in isolation
- [ ] I verify UI displays correctly
- [ ] I test end-to-end with realistic data

---

## Strategy 6: Use Dry-Run/Preview Modes

**Time: 30 minutes (to add) | Impact: Confidence in destructive operations**

### Goal
Verify logic before making irreversible changes.

### Implementation

```python
# Add --dry-run flag to destructive operations
def mark_tasks_abandoned(threshold=7, dry_run=False):
    candidates = find_candidates(threshold)
    
    if dry_run:
        # Show what would happen, don't do it
        print(f"Would abandon {len(candidates)} tasks:")
        for task in candidates:
            print(f"  - {task.title}")
        return
    
    # Actually do the operation
    for task in candidates:
        task.status = ABANDONED
    save()
```

### User Experience

```bash
# Preview first
$ python cli.py abandon --days 7 --dry-run
[DRY RUN] Would abandon 2 tasks:
  - Old Low Priority Task
  - Old Medium Priority Task
Run without --dry-run to actually mark as abandoned

# Then execute with confidence
$ python cli.py abandon --days 7
Marked 2 tasks as abandoned
```

### Benefits
- Users verify logic before committing
- Early error detection
- Confidence in correctness
- Easy rollback testing (compare dry-run output with actual)

### Success Criteria
- [ ] Dry-run shows what would happen accurately
- [ ] Actual execution matches dry-run preview
- [ ] No surprises when running for real
- [ ] Users feel confident in the operation

---

## Strategy 7: Think About Future Developers

**Time: 20 minutes | Impact: Code stays maintainable**

### Goal
Write code that future developers (including you in 6 months) can understand.

### Practices

**1. Clear Variable Names**
```python
# ❌ Bad
days_past = (datetime.now() - self.due_date).days

# ✅ Good
days_overdue = (datetime.now() - self.due_date).days
```

**2. Docstrings Explain WHY**
```python
# ❌ Bad
def is_overdue(self):
    """Check if task is overdue."""
    return self.due_date < datetime.now()

# ✅ Good
def is_overdue(self):
    """Check if task is overdue and not yet completed.
    
    Returns False for completed tasks even if delivered late,
    because completed work should not generate alerts.
    See: BUSINESS_RULES.md#Overdue Definition
    """
    return (self.due_date < datetime.now() and 
            self.status != TaskStatus.DONE)
```

**3. Comments at Decision Points**
```python
# ✅ Good
# Only abandon LOW/MEDIUM priority tasks; protect HIGH/URGENT
# (HIGH-priority work should never be abandoned)
to_abandon = [t for t in candidates 
              if t.priority in [LOW, MEDIUM]]
```

**4. Isolate Business Rules**
```python
# ✅ Good: Business rule in one place
def can_be_abandoned(self, threshold_days=7):
    """All abandonment logic in one method."""
    return (self.days_overdue() >= threshold_days and
            self.priority in [TaskPriority.LOW, TaskPriority.MEDIUM])

# ✅ Usage: Clear intent
if task.can_be_abandoned():
    mark_as_abandoned(task)
```

**5. Group Related Code**
```python
# ✅ Good organization
class TaskStatistics:
    def count_by_status(self): ...
    def count_by_priority(self): ...
    def count_overdue(self): ...
    def count_abandoned(self): ...
    # All statistics logic in one place
```

**6. Add Examples in Docstrings**
```python
def mark_overdue_tasks_as_abandoned(self, threshold_days=7, dry_run=False):
    """Mark old overdue tasks as abandoned.
    
    Args:
        threshold_days: Only abandon tasks overdue > N days (default 7)
        dry_run: If True, show what would happen (default False)
    
    Returns:
        (count, task_ids) - how many abandoned and their IDs
    
    Example:
        >>> count, ids = task_manager.mark_overdue_tasks_as_abandoned(dry_run=True)
        >>> print(f"Would abandon {count} tasks")
    
    Business Rule:
        - Only LOW and MEDIUM priority tasks
        - HIGH and URGENT priority are protected
        - Already abandoned tasks are skipped (idempotent)
    """
```

### When You'll Appreciate This
- In 6 months when you're debugging
- When a new dev joins the team
- When requirements change and code needs updating
- During code review when teammate asks "why did you do this?"

### Success Criteria
- [ ] A new developer can understand my code without asking
- [ ] Business rules are documented in code
- [ ] Integration points are clear
- [ ] Edge cases are handled and commented
- [ ] Future changes are easier because code is organized

---

## Quick Reference Checklist

### Before You Code
- [ ] Ran Strategy 1 (established geography)
- [ ] Ran Strategy 2 (read tests or wrote exploratory test)
- [ ] Ran Strategy 3 (found existing patterns)
- [ ] Ran Strategy 4 (asked clarifying questions)

### While You Code
- [ ] Ran Strategy 5 (implement & test in layers)
- [ ] Ran Strategy 6 (added --dry-run for safety)

### After You Code
- [ ] Ran Strategy 7 (wrote for future developers)
- [ ] Code review submitted
- [ ] Team feedback incorporated

---

## Common Mistakes to Avoid

| Mistake | Why It Hurts | How to Prevent |
|---------|-------------|---|
| Jumping to code before understanding | Rework, wrong architectural decisions | Do Strategy 1 first |
| Reinventing instead of reusing | 3x slower, inconsistent patterns | Use Strategy 3 |
| Coding before clarifying requirements | Wrong features, rework, frustration | Use Strategy 4 |
| Testing only at the end | Hard to debug, cascading failures | Use Strategy 5 |
| Trusting your logic without preview | Ship bugs to production | Use Strategy 6 |
| Writing inscrutable code | Team frustration, future maintenance nightmares | Use Strategy 7 |

---

## Time Investment Payoff

| Strategy | Setup Time | Time Saved | ROI |
|----------|-----------|-----------|-----|
| Strategy 1: Geography | 15 min | 2 hours | 8x |
| Strategy 2: Tests | 20 min | 1 hour | 3x |
| Strategy 3: Patterns | 30 min | 2 hours | 4x |
| Strategy 4: Questions | 30 min | 1.5 hours | 3x |
| Strategy 5: Layers | +30 min | 1 hour | 1.5x |
| Strategy 6: Dry-run | 30 min | 1 hour | 2x |
| Strategy 7: Future devs | 20 min | 2 hours (later) | 6x |
| **Total** | **2.5 hours** | **10+ hours** | **4x** |

---

## Real-World Example: Task Abandonment Implementation

**How these strategies were applied:**

1. ✅ **Strategy 1**: Identified that business logic lives in models.py
2. ✅ **Strategy 2**: Read how `is_overdue()` works to understand status rules
3. ✅ **Strategy 3**: Found `get_tasks()` pattern for filtering, modeled abandonment on it
4. ✅ **Strategy 4**: Asked about HIGH/URGENT protection, rerun behavior
5. ✅ **Strategy 5**: Models → Storage → App → CLI (tested each layer)
6. ✅ **Strategy 6**: Added `--dry-run` to preview before actual abandonment
7. ✅ **Strategy 7**: Documented business rule in code comments

**Result:** Feature implemented correctly in 3 hours with zero rework

---

## Next Steps

1. Pick a feature you want to implement
2. Go through each strategy in order
3. Document your experience (what worked, what didn't)
4. Mentor the next developer using these strategies
5. Refine these strategies based on your team's culture

**Remember:** These aren't just task-manager specific. You'll use these strategies for decades, across dozens of codebases.

---

*Based on how senior developers think. Practice these now; they compound over your career.*

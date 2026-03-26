# How to Use This Project as a Learning Tool

## Overview

The Task Manager project is specifically designed as a **learning-friendly codebase** for junior developers. This guide explains how to maximize your learning.

---

## 🎯 What You'll Learn

By working through this project systematically, you'll master:

- **Layered Architecture**: Understanding separation of concerns in real code
- **Domain Modeling**: Translating business requirements into data structures
- **Code Navigation**: Finding your way in unfamiliar codebases
- **Feature Implementation**: From requirements to tested code
- **Business Logic**: Thinking beyond syntax to understand user intent
- **Testing Strategy**: Verifying correctness without formal test frameworks

---

## 📚 Learning Path

### Phase 1: Understand the Structure (1-2 hours)
**Goal**: Build a mental map of the codebase

**Steps:**
1. Read [README.md](README.md) to understand the project's purpose
2. Follow the prompts in order from [LEARNING_JOURNEY.md](LEARNING_JOURNEY.md) → **"Initial vs. Final Understanding"**
3. List all files and write one-sentence descriptions
4. Trace code execution: `python -m python.cli list` → follow the call stack
5. Answer: "What is the purpose of each file?"

**Success criteria:** You can explain the 4-layer architecture without looking at code

---

### Phase 2: Explore Existing Features (2-3 hours)
**Goal**: Understand how features are implemented

**Steps:**
1. Read [ONBOARDING_GUIDE.md](ONBOARDING_GUIDE.md) → Strategy 2 & 3 (Tests & Patterns)
2. Run: `python -m python.cli create "test" -d "desc" -p 2 -u 2026-12-31`
3. Run: `python -m python.cli list`
4. Run: `python -m python.cli export tasks.csv`
5. For each command, trace the code: CLI → App → Storage → Models

**Success criteria:** You understand how create/list/export commands work end-to-end

---

### Phase 3: Understand the Domain (2-3 hours)
**Goal**: Think like a domain architect, not just a coder

**Steps:**
1. Read [LEARNING_JOURNEY.md](LEARNING_JOURNEY.md) → **"Most Valuable Insights"** sections
2. Answer the 5 test questions (with answers provided)
3. Create scenarios: "What if someone marks a task DONE after 30 days?"
4. Read `models.py` and understand business rules in code

**Success criteria:** You can explain why `is_overdue()` returns False for completed tasks

---

### Phase 4: Implement a Feature (4-6 hours)
**Goal**: Write production-quality code following project patterns

**Steps:**
1. Pick a feature from "Potential Enhancements" (below)
2. Follow [ONBOARDING_GUIDE.md](ONBOARDING_GUIDE.md) → Strategy 1-4 (Planning & Questions)
3. Generate clarifying questions; ask your team
4. Implement in layers (models → storage → app → cli)
5. Test with realistic data scenarios
6. Get code review from senior dev

**Success criteria:** Feature works; code follows project patterns; team approves

---

## 💡 Suggested Learning Features

### Easy (Great for learning)
- [ ] **Add task archival**: Tasks can be manually moved to "archived" status
  - Learning: Basic status addition, filtering, CLI command
  - Estimated time: 2 hours
  
- [ ] **Show task age**: Display how long a task has been in current status
  - Learning: Temporal calculations, display formatting
  - Estimated time: 1 hour

### Medium (Challenges you)
- [ ] **Search by keyword**: `python cli.py search "login"` finds tasks with matching title/description
  - Learning: String matching, filtering logic
  - Estimated time: 2-3 hours

- [ ] **Relative due dates**: `python cli.py create "task" --due "tomorrow"` or `--due "in 3 days"`
  - Learning: Date parsing, user experience design
  - Estimated time: 3 hours

### Hard (Stretches you)
- [ ] **Task recurrence**: Completed tasks can create a follow-up automatically
  - Learning: Complex state transitions, side effects in business logic
  - Estimated time: 4-5 hours

- [ ] **Task dependencies**: Mark task B as "blocked by" task A; prevent marking blocked tasks DONE
  - Learning: Relationships between entities, validation rules
  - Estimated time: 5-6 hours

---

## 🧪 Testing Your Learning

### Self-Check Questions

After Phase 3, you should answer yes to:
- [ ] Can I explain why each file exists?
- [ ] Can I trace a user command → final output?
- [ ] Can I find where business rules live in code?
- [ ] Can I predict what happens if I modify `is_overdue()`?
- [ ] Can I design a new feature without guidance?

---

## 🛠️ Reference Materials

| Resource | Purpose | Time |
|----------|---------|------|
| [README.md](README.md) | Project overview & setup | 5 min |
| [LEARNING_JOURNEY.md](LEARNING_JOURNEY.md) | Transformation story & insights | 20 min |
| [ONBOARDING_GUIDE.md](ONBOARDING_GUIDE.md) | 7 strategies for unfamiliar code | 25 min |
| [models.py](python/models.py) | Domain model & business rules | 15 min |
| [storage.py](python/storage.py) | Data persistence & filtering | 20 min |
| [app.py](python/app.py) | Service layer orchestration | 15 min |
| [cli.py](python/cli.py) | User interface & argument parsing | 20 min |

---

## 👥 Getting Help

### If You're Stuck
1. **"I don't understand the codebase structure"** → Re-read Phase 1 steps; draw a diagram
2. **"I don't know where to implement a feature"** → Use ONBOARDING_GUIDE.md Strategy 1-3
3. **"My implementation doesn't work"** → Use ONBOARDING_GUIDE.md Strategy 2 (test first)
4. **"I don't understand a business rule"** → Read LEARNING_JOURNEY.md test questions
5. **"I need code review"** → Share with team; ask specific questions about your design

### Recommended Pairing
- Phase 1: **Solo** (establish independence)
- Phase 2: **With peer** (learn through discussion)
- Phase 3: **With senior dev** (validate understanding)
- Phase 4: **With mentor** (implement together first time)

---

## 📈 Success Metrics

You've mastered this codebase when you can:

✅ Implement a feature from requirements to testing **without asking where things go**  
✅ Explain why code is organized the way it is **in business terms**  
✅ Spot where a new requirement fits **by reading code patterns**  
✅ Generate meaningful test scenarios **before writing code**  
✅ Make architectural decisions **aligned with project philosophy**  

---

## 🎓 Beyond This Project

The skills you learn here apply to any codebase:

- **Layered architecture** → found in web apps, backends, desktop apps
- **Domain modeling** → critical in any business system (billing, auth, workflows)
- **Code navigation** → essential for open-source contributions
- **Business logic** → separates junior devs from seniors
- **Feature implementation** → career foundation

---

## 📝 When You're Done

1. **Commit your learning journey**: `git add LEARNING_JOURNEY.md && git commit -m "my learning journey"`
2. **Update this guide**: Add what actually helped vs. what didn't
3. **Mentor the next person**: Use your experience to help them learn faster
4. **Pay it forward**: Document your favorite insights in code comments

---

*This learning-focused project design is inspired by how senior developers actually work with unfamiliar code. Practice these skills now; they'll serve you for decades.*

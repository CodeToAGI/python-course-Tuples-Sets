# CodeToAGI - Python Mastery Course 🐍

## From Zero to Agentic AI — One Episode at a Time

Welcome to the official **CodeToAGI Python Course** repository! 

This course takes you from absolute beginner to building AI systems through daily, bite-sized episodes. Each episode includes:
- 📹 Full video tutorial on YouTube
- 💻 Complete project code
- 🧪 Hands-on challenges with solutions
- 🚀 Real-world applications

---

## 📺 EPISODE 10: Tuples & Sets — Immutable and Unique Data

[![Watch Episode 10](https://img.youtube.com/vi/YOUR_VIDEO_ID/maxresdefault.jpg)](https://youtu.be/YOUR_VIDEO_ID)

### 🎯 What You'll Learn
- **Tuples** — Ordered, immutable collections (parentheses `()`)
- **Sets** — Unordered, unique-only collections (curly braces `{}`)
- List vs Tuple vs Set — When to use which
- Tuple unpacking — Assign multiple variables in one line
- Set operations — Union (`|`), Intersection (`&`), Difference (`-`)
- Lightning-fast membership checking with sets (O(1) vs O(n))

### 📁 Files in This Episode

| File | Description |
|------|-------------|
| `ep10_tuples_sets_project.py` | Complete project + challenge solutions |

### 🧪 Episode 10 Challenge: Student Attendance Tracker

```python
# YOUR TASK — Try it yourself first!
class_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
attended = {"Monday", "Wednesday", "Friday"}

# Find missed days using set difference
missed = set(class_days) - attended

print(f"Total days: {len(class_days)}")
print(f"Attended: {len(attended)}")
print(f"Missed: {len(missed)} — {missed}")

# ============================================================
# CodeToAGI -- Episode 10: Tuples and Sets
# GitHub : https://github.com/CodeToAGI/python-course
# ============================================================
# Try the challenge yourself FIRST before looking at this!
# ============================================================

# Part 1: Unique Word Counter (shown in video)
def word_counter(text):
    """Analyze text using lists, sets, and dicts."""
    words  = text.lower().split()      # list -- all words in order
    unique = set(words)                # set  -- removes duplicates instantly

    result = {
        "total_words":  len(words),
        "unique_words": len(unique),
        "duplicates":   len(words) - len(unique),
    }

    print("\n" + "="*40)
    print("  CodeToAGI -- Word Counter")
    print("="*40)
    for k, v in result.items():
        print(f"  {k:<16}: {v}")

    sorted_words = sorted(unique)
    print(f"\n  Unique words ({len(sorted_words)}):")
    print(f"  {sorted_words}\n")


# Part 2: Student Attendance Tracker (your challenge!)
def attendance_tracker():
    """Track attendance using tuples and sets."""
    # Tuple -- fixed school days (never changes)
    class_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

    # Set -- days attended (try changing these)
    attended = {"Monday", "Wednesday", "Thursday", "Friday"}

    # Set difference -- find missed days
    missed = set(class_days) - attended

    print("\n" + "="*40)
    print("  Student Attendance Report")
    print("="*40)
    print(f"  Total class days : {len(class_days)}")
    print(f"  Days attended    : {len(attended)}")
    print(f"  Days missed      : {len(missed)}")
    print(f"  Missed days      : {sorted(missed)}")

    # Membership check using 'in' on a set -- instant!
    if "Monday" in attended:
        print("  Monday          : Present")
    else:
        print("  Monday          : Absent")
    print()


# Part 3: Set operations demo
def set_operations_demo():
    """Demonstrate union, intersection, difference."""
    python_students = {"Ali", "Sara", "Umar", "Fatima"}
    ml_students     = {"Sara", "Fatima", "Zara", "Ahmed"}

    print("\n" + "="*40)
    print("  Set Operations Demo")
    print("="*40)
    print(f"  Python class : {sorted(python_students)}")
    print(f"  ML class     : {sorted(ml_students)}")
    print(f"  Union (all)  : {sorted(python_students | ml_students)}")
    print(f"  Both classes : {sorted(python_students & ml_students)}")
    print(f"  Python only  : {sorted(python_students - ml_students)}")
    print(f"  ML only      : {sorted(ml_students - python_students)}\n")


# Run all projects
if __name__ == "__main__":
    sample = "python is great python is powerful python is fun"
    word_counter(sample)
    attendance_tracker()
    set_operations_demo()

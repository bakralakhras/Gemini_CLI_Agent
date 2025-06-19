import os

def find_matching_file(working_directory, expression):
    working_directory = os.path.abspath(working_directory)
    scored = []

    indicators = [
        "def evaluate(",
        "evaluate(self, expression)",
        "self.operators",
        "self.precedence",
        "re.findall",
        "tokens",
        "+", "-", "*", "/"
    ]

    for root, _, files in os.walk(working_directory):
        for fname in files:
            if fname.endswith(".py"):
                full_path = os.path.join(root, fname)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        score = sum(indicator in content for indicator in indicators)
                        if score >= 2:
                            rel_path = os.path.relpath(full_path, working_directory)
                            scored.append((score, rel_path))
                except Exception:
                    continue

    if not scored:
        return "No matching Python files found."

    # Sort by score descending
    scored.sort(reverse=True)
    top_score, top_file = scored[0]
    return f"Best match: {top_file} (score: {top_score})"

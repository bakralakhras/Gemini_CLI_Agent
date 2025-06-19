from find_matching_file import find_matching_file

# Use a relative path pointing to the actual calculator folder
working_dir = "../calculator"
expression = "3+7*2"  # Could be any expression — we’re testing general logic detection

# Run the function
print("=== Matching Files for Expression Evaluation ===")
result = find_matching_file(working_dir, expression)
print(result)

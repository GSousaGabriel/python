results = {"Paul": 9, "Peter": 3, "Roger": 21}

print(results, len(results), results.get("Paul"), results["Roger"])

removed = results.pop("Peter")

print(removed, results)
def get_duplicated_items(items):
    seen = set()
    duplicated = []
    duplicated_set = set()

    for item in items:
        if item in seen and item not in duplicated_set:
            duplicated.append(item)
            duplicated_set.add(item)
        else:
            seen.add(item)

    return duplicated


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"duplicated items: {get_duplicated_items(items)}")

# Time complexity: O(n)
# Space complexity: O(n)
    
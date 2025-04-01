def normalize_name(name):
    """Remove hyphens and convert to lowercase."""
    return name.replace("-", "").lower()

if __name__ == "__main__":
    user_input = input("Enter a countryball name: ")
    normalized_name = normalize_name(user_input)
    print(f"Normalized Name: {normalized_name}")

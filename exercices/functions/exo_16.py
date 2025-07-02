def name_constructor(first_name : str, last_name : str) -> str :
    return f"{first_name.strip().title()} {last_name.strip().title()}"

print(name_constructor("John", "Doe"))
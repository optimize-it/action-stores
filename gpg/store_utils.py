def remove_backticks(string):
    if string.startswith("```") and string.endswith("```"):
        string = string.lstrip("```").rstrip("```")
    return string
def extract_title(markdown):
    h1_text = ""
    for line in markdown.splitlines():
        stripped = line.strip()
        if len(stripped) >= 2 and stripped[0] == "#" and stripped[1] == " ":
            h1_text = line.split("#", 1)[1].strip()
            break
    
    if h1_text == "":
        raise ValueError(f"h1 Heading not found in document: {markdown}")
    
    return h1_text
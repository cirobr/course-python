def read_book(title_path):
    # modified reading of text file (preferred)
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()

    # remove \n e \r
    text = seq.replace("\n", "").replace("\r", "")
    
    return text

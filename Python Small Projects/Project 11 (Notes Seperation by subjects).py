with open("notes.txt", "r") as f:
    parts = f.read().split(",")
    print(parts)
    print(f"English Notes: \n{parts[0]}\n")
    print(f"Hindi Notes: \n{parts[1]}")
    # print("Parts   : ", parts)
    # print("Parts[1]: ", parts[1])
    # print("Parts[1]split hindi: ", parts[1].split("Hindi")[0].strip())
    # if len(parts) > 1:
    #     english_notes = parts[1].split("Hindi")[0].strip()
    #     print(english_notes)
    # hindi notes
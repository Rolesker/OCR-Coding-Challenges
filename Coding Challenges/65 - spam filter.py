def spamify(menu):
    output=[]
    for i in menu:
        modified_text="spam "
        for j in i.split():
            modified_text+=j+" spam "
        modified_text=modified_text.rstrip()
        output.append(modified_text)
    return output


print(spamify(["tomato soup","pizza","spam","fish and chips"]))

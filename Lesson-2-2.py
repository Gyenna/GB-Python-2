sentence = ["в", "5", "часов", "17", "минут", "температура", "воздуха", "была",
            "+5", "градусов"]
sentence_2 = []
for el in sentence:
    if el.isdigit():
        sentence_2.extend(["'", f"{int(el):02}", "'"])
    elif el.startswith("+") or el.startswith("-"):
        if el[1:].isdigit():
            sentence_2.extend(["'", f"{el[0]}{int(el[1]):02}", "'"])
        else:
            sentence_2.append(el)
    else:
        sentence_2.append(el)
    sentence_2.append(" ")
sentence_2 = "".join(sentence_2)
print(sentence_2)

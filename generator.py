#❤️🤍
s = ""
for i in range(7):
    for j in range(7):
        s += "🤍🤍🤍🤍🤍🤍🤍\n" * i + "🤍" * j + "❤️" * (7 - j) + "\n" + "❤️❤️❤️❤️❤️❤️❤️\n" * (6 - i) + "-\n"

open('out.txt', 'w', encoding="utf-8").write(s)
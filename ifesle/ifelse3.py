def action_1():
    return "공격"

def action_2():
    return "방어"

commands = {
    "A": action_1,
    "B": action_2,
    "C": lambda: "도망"
}

key = "B"
result = commands.get(key, lambda: "잘못된 입력")()
print(result)
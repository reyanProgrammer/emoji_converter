msg = input("> ")
words = msg.split(" ")
emoji_map = {
    ":)": "😉",
    ":(": "🥺"
}
output = ""
for word in words:
    output += emoji_map.get(word, word)
print(output)


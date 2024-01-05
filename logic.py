import emoji


def print_all_emoji():
    emojis = emoji.EMOJI_DATA
    for emoji_str in emojis:
        print(emoji_str)


print_all_emoji()

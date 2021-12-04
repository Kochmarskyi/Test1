Text_user = str(input('Print the text: '))
words = Text_user.split(' ')
res = [w[::-1] if i % 1 != 1 else w for i, w in enumerate(words)]

print(' '.join(res))
input("\nEnter.")

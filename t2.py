name = str(input('P: '))

	
if __name__ == '__main__':
	def reverse_string(s):
		chars = list(s)

		for i in range(len(s) // 2):
			temp = chars[i]
			chars[i] = chars[len(s) - i - 1]
			chars[len(s) - i - 1] = temp

		return ''.join(chars)

print(name)
print(reverse_string(name))
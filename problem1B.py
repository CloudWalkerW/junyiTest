def reverse_each_word(sentence):
	input_split = sentence.split(" ")
	for i in range(len(input_split)):
		input_split[i] = input_split[i][::-1]
	return " ".join(input_split)


inputstr = input("請輸入字串：")
print(reverse_each_word(inputstr))

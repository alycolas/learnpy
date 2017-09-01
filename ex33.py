def numberlist(last, interval):
	i = 0
	numbers = []

	while i < int(last):
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + int(interval)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num


numberlist(raw_input("> "), raw_input("> "))

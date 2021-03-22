

disk_words = open("disk_words.txt", "r")
linux_words = open("linux_words.txt", "r")
missing_words = open("missing_words.txt", "w")

disk_lines = disk_words.readlines()
linux_lines = linux_words.readlines()

for line in linux_lines:
	if line not in disk_lines:
		missing_words.write(line)


disk_words.close()
linux_words.close()
missing_words.close()


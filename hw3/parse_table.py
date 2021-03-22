tabled_file = open("tabled_file.txt", "w")
stitched_file = open("stitched.txt", "r")

tabled_file.write("|        *IP*        |        *Date*        |        *Time*        |        *REQUEST TYPE*        |        *REQUESTED FILE*        |        *response code*        |\t\n")

stitched_lines = stitched_file.readlines()

for line in stitched_lines:

	ip, line_2 = line.split("- -", 1)
	date, line_3 = line_2.split("]", 1)
	date = date[2:]
	date, time = date.split(":", 1)
	time, trash = time.split("-", 1)
	
	rest = line_3.split(" ");
	req = rest[1]
	req = req[1:]
	
	reqfile = rest[2]
	resp = rest[4] + " " + rest[5]
	
	
	
	tabled_file.write("|    " + ip + "    |    " + date + "    |    " + time + "    |        " + req + "        |       " + reqfile + "        |        " + resp.strip() + "        |\t\n")

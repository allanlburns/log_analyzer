import re


# with open("~/Desktop/coreserver.log") as file:
# 	file.read()

file = open("./coreserver.log")
lines = file.readlines()
errors = []

for line in lines:
# 	print(line)
	error_regex = re.compile(r'\s\[ERROR\]\[\]*')
	match = error_regex.search(line)
	if match:
		errors.append(line)
		# print(line)

print(f"Found {len(errors)} errors.")
if errors:
	for error in errors:
		print(error)



file.close()

# print("Is file closed? " + file.closed())
# print(lines[-1])
#print("Readlines is a " + str(type(lines)))
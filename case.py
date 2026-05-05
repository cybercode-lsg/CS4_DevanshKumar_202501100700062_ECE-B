# ---------- Task 1: Basic File Reading ----------
file = open("CS4.txt", "r")

# Using read()
content = file.read()
print("Full Content:\n", content)

# Reset pointer
file.seek(0)

# Using readline()
print("\nUsing readline():")
print(file.readline())
print(file.readline())

# Reset pointer
file.seek(0)

# Using readlines()
lines = file.readlines()

print("\nTotal number of lines:", len(lines))
print("\nFirst 2 lines:")
print("".join(lines[:2]))

print("\nLast 2 lines:")
print("".join(lines[-2:]))

file.close()


# ---------- Task 2: Log Classification ----------
file = open("CS4.txt", "r")
lines = file.readlines()

log_count = {"INFO": 0, "WARNING": 0, "ERROR": 0}

for line in lines:
    if "INFO" in line:
        log_count["INFO"] += 1
    if "WARNING" in line:
        log_count["WARNING"] += 1
    if "ERROR" in line:
        log_count["ERROR"] += 1

print("\nLog Count:", log_count)

file.close()


# ---------- Task 3: Write Filtered Files ----------
info_file = open("info_logs.txt", "w")
warning_file = open("warning_logs.txt", "w")
error_file = open("error_logs.txt", "w")

for line in lines:
    if "INFO" in line:
        info_file.write(line)
    if "WARNING" in line:
        warning_file.write(line)
    if "ERROR" in line:
        error_file.write(line)

info_file.close()
warning_file.close()
error_file.close()


# ---------- Task 4: Search Feature ----------
keyword = input("\nEnter keyword to search: ")

file = open("CS4.txt", "r")
lines = file.readlines()

results = []

print("\nMatching Lines:")
for line in lines:
    if keyword in line:
        print(line.strip())
        results.append(line)

# Save results
search_file = open("search_result.txt", "w")
search_file.writelines(results)
search_file.close()

file.close()


# ---------- File Pointer (seek) Operations ----------
file = open("CS4.txt", "r")

# Read first 50 characters
print("\nFirst 50 characters:")
print(file.read(50))

# Move to beginning
file.seek(0)
print("\nAfter seek(0):")
print(file.read(50))

# Move to middle
file.seek(0)
content = file.read()
middle = len(content) // 2

file.seek(middle)
print("\nFrom middle:")
print(file.read(50))

# Move to last 100 characters
file.seek(0, 2)  # Go to end
file.seek(file.tell() - 100)

print("\nLast 100 characters:")
print(file.read())

file.close()

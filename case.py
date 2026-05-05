# CS4_YourName_RollNo_Section.py

# Task 1: Basic File Reading
with open("CS4.txt", "r") as f:
    content = f.read()
    f.seek(0)
    lines = f.readlines()

print("Total number of lines:", len(lines))
print("First 2 lines:", lines[:2])
print("Last 2 lines:", lines[-2:])

# Task 2: Log Classification
log_counts = {"INFO":0, "WARNING":0, "ERROR":0}
for line in lines:
    for key in log_counts:
        if key in line:
            log_counts[key] += 1
print("Log counts:", log_counts)

# Task 3: Write Filtered Files
with open("info_logs.txt", "w") as f_info, \
     open("warning_logs.txt", "w") as f_warn, \
     open("error_logs.txt", "w") as f_err:
    for line in lines:
        if "INFO" in line:
            f_info.write(line)
        elif "WARNING" in line:
            f_warn.write(line)
        elif "ERROR" in line:
            f_err.write(line)

# Task 4: Search Feature
keyword = input("Enter keyword to search (INFO/WARNING/ERROR): ")
matches = [line for line in lines if keyword in line]
print("Matching lines:")
for m in matches:
    print(m.strip())

with open("search_result.txt", "w") as f_search:
    f_search.writelines(matches)

# File Pointer Operations
with open("CS4.txt", "r") as f:
    print("First 50 chars:", f.read(50))

    f.seek(0)
    print("Seek to beginning:", f.read(50))

    f.seek(len(content)//2)
    print("Seek to middle:", f.read(50))

    f.seek(-100, 2)
    print("Last 100 chars:", f.read())

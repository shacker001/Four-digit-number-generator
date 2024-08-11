with open("file.txt", "w") as file:
    for i in range(1000, 10000):
        file.write(f"{i}\n")

# Reading back to check the content
with open("file.txt", "r") as file:
    lines = file.readlines()
    print(f"Total numbers written: {len(lines)}")
    print(f"First number: {lines[0].strip()}")
    print(f"Last number: {lines[-1].strip()}")


reports = open("day2.txt", "r").readlines()

safe_count = 0

for i, line in enumerate(reports):
    report = line.strip("\n").replace(" ", "")

    print(f"Report[{i+1}] -> ", end="")

    safe = True

    for i in range(len(report)-1):

        increasing = int(report[0]) < int(report[1])

        print(f"{report[i]} ", end="")
        if i == 3: print(f"{report[4]} ", end="")

        if not increasing:
            not_decreasing = int(report[i-1]) > int(report[i]) and int(report[i]) < int(report[i+1])

            if i > 0 and not_decreasing:
                safe = False
                continue

            diff = int(report[i]) - int(report[i+1])

            if diff < 1 or diff > 3: safe = False


        elif increasing:
            not_inscreasing = int(report[i-1]) < int(report[i]) and int(report[i]) > int(report[i+1])

            if i > 0 and not_inscreasing:
                safe = False
                continue

            diff = int(report[i+1]) - int(report[i])

            if diff < 1 or diff > 3: safe = False

    if safe:
        print(": SAFE")
        safe_count += 1
    else:
        print(": UNSAFE")

print(f"{safe_count} reports are safe")


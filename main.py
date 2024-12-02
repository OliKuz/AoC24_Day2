# read each lane into an array
# go checking the adjacent numbers within the lane 
# check for the follwoing conditions:
    ## The levels are either all increasing or all decreasing.
    ## Any two adjacent levels differ by at least one and at most three.
# make total count of good reports

def main():
    input_file = open("input.txt", "r")

    num_valid = 0

    for line in input_file:
        lane = line.split()
        report = []
        for i in range(0, len(lane)):
            report.append(int(lane[i]))
        print(report)

        if check_report(report):
            num_valid += 1
    
    print("Number of valid reports: ", num_valid)

def check_report(report):

    increasing = False

    if report[0] < report[1]:
        increasing = True

    for i in range(0, len(report) - 1):

        if increasing:
            if report[i] >= report[i + 1]:
                return False
        else:
            if report[i] <= report[i + 1]:
                return False
        
        if abs(report[i] - report[i + 1]) > 3:
            return False
        
    return True


if __name__ == "__main__":   
    main()


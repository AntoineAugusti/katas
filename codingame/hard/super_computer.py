
N = int(raw_input())
calculations = []
for _ in xrange(N):
    startDay, duration = [int(j) for j in raw_input().split()]
    endDay = duration + startDay - 1
    calculations.append([startDay, duration, endDay])


def sortEndDate(x, y):
    # Sort the list thanks to the end of the computation
    if (x[2] > y[2]):
        return 1
    elif (x[2] < y[2]):
        return -1
    else:
        return 0


def nbScientists(calculations):
    count = 0
    upperBound = -1
    for c in calculations:
        # If the beginning of the calculation is not in
        # the already booked period
        if (upperBound < c[0]):
            # Add this calculation
            count += 1
            # The upper bound is now its end date
            upperBound = c[2]
    return count

calculations.sort(sortEndDate)
print nbScientists(calculations)

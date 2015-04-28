from sys import exit

nbOods = int(raw_input())
giftPrice = int(raw_input())

# Read the budget for each Ood
budgets = []
for _ in xrange(nbOods):
    budgets.append(int(raw_input()))

# Check that we can pay for the gift
if (sum(budgets) < giftPrice):
    print 'IMPOSSIBLE'
    exit()

nbOodsWithMoney = nbOods
toPayList = [0] * nbOodsWithMoney
# Loop while the cost requires more than 1 unit from each
# remaining Ood
while (giftPrice > nbOodsWithMoney):
    # Determine the ideal fair split given the number of Oods left
    fairAmount = giftPrice / nbOodsWithMoney
    for i, budget in enumerate(budgets):
        if budget == 0:
            continue
        else:
            # Determine how much this Ood will pay
            if (budget < fairAmount):
                toPay = budget
            else:
                toPay = fairAmount
            budgets[i] = budgets[i] - toPay
            # If the Ood ran out of money, remember that
            if (budgets[i] == 0):
                nbOodsWithMoney = nbOodsWithMoney - 1
            # Update the price of the gift after the Ood paid
            giftPrice = giftPrice - toPay
            toPayList[i] = toPayList[i] + toPay

# We still have some adjustements to make
# Each remaining Ood must pay 1 unit or nothing
if (giftPrice > 0):
    for i in range(nbOods)[::-1]:
        if (giftPrice > 0 and budgets[i] > 0):
            budgets[i] = budgets[i] - 1
            giftPrice = giftPrice - 1
            toPayList[i] = toPayList[i] + 1

# Present the list to pay in ascending order
toPayList.sort()
for toPay in toPayList:
    print toPay

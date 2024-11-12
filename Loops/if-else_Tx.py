# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

Income = float(input("Enter you income : "))


if Income < 85528:
    tax = Income * 0.18 - 556.02
else:
     tax = ((85528)*0.18-556.02) + ((Income-85528)*0.32-556.02)

tax = round(tax,00)
print("The tax on",Income,"is",tax)
#14839.02




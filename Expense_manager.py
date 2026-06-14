
ExpenseList = []

print("--------MENU--------")
print("1.ADD EXPENSE")
print("2.VIEW ALL EXPENSE")
print("3.TOTAL EXPENSE")
print("4.EXIT")

while True:
  choice = input("Enter Your Choice: ")

  if choice == "1":
    date = input("enter date for expense")
    category = input("enter type of expense(like -dress,makeup,food,etc)")
    detail = input("enter more detail")
    amount = input("enter amount of expense")
    
    expense = {
      "date": date,

      "category": category,
      "description": detail,
      "amount": amount
    }
    ExpenseList.append(expense)
    print("\n✅ Expense added successfully!")
    
  elif choice == "2":
    if len((ExpenseList)) == 0:
      print("no expense")
    else:
      print("\n--- All Expenses ---")
      i = 1
      for e in expense:
        print(f"{i}. {e['date']} | {e['category']} |{e['description']} | ₹{e['amount']}")
        i += 1
  elif choice == "3":
    total = 0
    for e in ExpenseList:
      total = total + e["amount"]
    print(f"\n💰 Total Spending = ₹{total}")

  elif choice == "4":
    print("\n👋 Thanks for using Expense Tracker! Bye!")
    break
  else:
    print("\n❌ Invalid choice. Please try again.")
    continue

    


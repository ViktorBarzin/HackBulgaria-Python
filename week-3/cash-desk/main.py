from cashdesk import Bill, BillBatch, CashDesk

values = [10, 20, 50, 50, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

cashd = CashDesk()
cashd.take_money(batch)

print(cashd.inspect())


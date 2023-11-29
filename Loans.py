class Loan:
    def __init__(self, principal, interest_rate, term):
        self.principal = principal
        self.interest_rate = interest_rate
        self.term = term

    def calculate_monthly_payment(self):
        monthly_interest_rate = self.interest_rate / 100 / 12
        num_months = self.term

        # Monthly payment formula for a fixed-rate loan
        monthly_payment = (self.principal * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -num_months)

        return monthly_payment

# Example usage:
loan_amount = int(input("How much would you like to recieve?"))
interest_rate = 5.0  # Example annual interest rate
loan_term = 12  # Example loan term in months

# Create a Loan instance
loan = Loan(loan_amount, interest_rate, loan_term)

# Calculate and print the monthly payment
monthly_payment = loan.calculate_monthly_payment()
print(f"Loan amount: ${loan.principal}")
print(f"Annual interest rate: {loan.interest_rate}%")
print(f"Loan term: {loan.term} months")
print(f"Monthly payment: ${monthly_payment:.2f}")

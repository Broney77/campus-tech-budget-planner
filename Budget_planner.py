 # ==========================================
# PROJECT: GHANA CEDI TECH BUDGET PLANNER
# AUTHOR: BOADU OSEI OWUSU BRONEY
# DESCRIPTION: A script tracking student savings goals for campus tech.
# ==========================================

# STEP 1: INITIAL DATA (VARIABLES)
target_laptop_price = 7000
current_savings = 1500
monthly_savings_target = 500

# STEP 2: CALCULATIONS & EVALUATION
remaining_balance = target_laptop_price - current_savings
months_needed = remaining_balance / monthly_savings_target

# STEP 3: CONSOLE PRINTING (THE DIGITAL DASHBOARD)
print("==================================================")
print("          CAMPUS TECH BUDGET DASHBOARD            ")
print("==================================================")
print("Target Laptop Cost   : GH₵", target_laptop_price)
print("Current Savings Fund : GH₵", current_savings)
print("--------------------------------------------------")
print("Remaining Balance    : GH₵", remaining_balance)
print("Savings Goal Rate    : GH₵", monthly_savings_target, "/ month")
print("--------------------------------------------------")
print("ESTIMATED TIMELINE   :", months_needed, "months")
print("==================================================")
print("Keep pushing! Your tech goals are within reach. 🚀")
print("==================================================")

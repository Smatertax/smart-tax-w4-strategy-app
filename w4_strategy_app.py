
import streamlit as st

st.set_page_config(page_title="Smart Tax W-4 Paycheck vs Refund Helper")

st.title("💼 Smart Tax W-4 Strategy Helper")
st.markdown("Not sure if you want more **money in your paycheck** now or a **bigger refund later**? Let's help you decide based on your numbers.")

# Input fields
st.subheader("Enter Your Info Below")
yearly_income = st.number_input("Annual Gross Income ($)", min_value=0)
filing_status = st.selectbox("Filing Status", ["single", "head_of_household", "married"])
current_withholding = st.number_input("Current Estimated Total Withholding ($)", min_value=0)
monthly_budget_gap = st.number_input("How much are you short per month? ($)", min_value=0)

# Logic to estimate impact
def w4_analysis(income, withheld, filing_status, monthly_gap):
    # Very simplified tax estimate
    deduction = {"single": 13850, "head_of_household": 20800, "married": 27700}.get(filing_status, 13850)
    taxable_income = max(0, income - deduction)
    est_tax = taxable_income * 0.1  # flat estimate

    refund = withheld - est_tax
    paycheck_gain = refund / 12 if refund > 0 else 0

    decision = "ADJUST" if paycheck_gain >= monthly_gap else "LEAVE"

    return refund, paycheck_gain, decision

# Button
if st.button("Evaluate My W-4 Strategy"):
    refund, monthly_gain, recommendation = w4_analysis(yearly_income, current_withholding, filing_status, monthly_budget_gap)

    st.markdown("---")
    st.subheader("🧾 Results")
    st.write(f"💰 Estimated Tax Refund: **${refund:,.2f}**")
    st.write(f"💵 Potential Monthly Paycheck Increase: **${monthly_gain:,.2f}**")

    if recommendation == "ADJUST":
        st.success("✅ You might consider adjusting your W-4 to increase your take-home pay now.")
        st.markdown("🔁 [Use the IRS W-4 Estimator](https://apps.irs.gov/app/tax-withholding-estimator) to make the changes.")
    else:
        st.info("📌 Keeping your current W-4 may be best if you need that refund for big expenses or savings.")

st.markdown("---")
st.caption("Powered by Smart Tax – Helping You Make Tax-Smart Decisions Year Round.")

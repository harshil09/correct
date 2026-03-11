import random
import pandas as pd
import streamlit as st

from ATM_BANKING import CheckingAccount, SavingsAccount

df=pd.read_csv("C:/Users/harsh/OneDrive/Desktop/db.csv")
print(df.head())
print(df.dtypes)

#APP_ACCOUNT_NUMBER = 12345678
#APP_PIN = 1234

st.set_page_config(
    page_title="Banking Application",
    page_icon= "💰",
    layout="centered"

)

def _init_state() -> None:
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("account", None)
    st.session_state.setdefault("account_type", "Savings")
    #st.session_state.setdefault("initial_balance", random.randint(100, 10000))
    st.session_state.setdefault("initial_balance")
    st.session_state.setdefault("last_message", "")



def _reset() -> None:
    for k in [
        "logged_in",
        "account",
        "account_type",
        "initial_balance",
        "last_message",
    ]:
        if k in st.session_state:
            del st.session_state[k]
    st.rerun()


_init_state()

st.markdown(
    """
    <h1 style='text-align: center; color:#034f84;'>
        🏦 Simple Banking System
    </h1>
    <p style='text-align: center; font-size:15px; color:#92a8d1;'>
        Manage your account with ease
    </p>
    """,
    unsafe_allow_html=True
)
#st.title("Simple Banking System")

with st.sidebar:
    st.subheader("Session")
    if st.session_state["logged_in"]:
        st.success("Logged in")
        if st.button("Reset / Logout"):
            _reset()
    else:
        st.info("logged out")


if not st.session_state["logged_in"]:
    st.subheader("🧑‍💻 Login")
    with st.form("login_form", clear_on_submit=False):
        accnumber=st.text_input("Account Number 💳", value="")
        pin=st.text_input("PIN 🔐", value="", type="password")
        #user=df[(df["acc_num"] == accnumber) & (df["acc_pin"]==pin)]
        #acc_number_raw = st.text_input("Account number", value="")
        #pin_raw = st.text_input("PIN", value="", type="password")
        submitted = st.form_submit_button("Login")
        #st.success("Login successful")

    if submitted:
        try:
            #acc_number = int(acc_number_raw.strip())
            #pin = int(pin_raw.strip())
            acc_number = int(accnumber.strip())
            pi = int(pin.strip())
        except ValueError:
            st.error("Please enter numeric account number and PIN.")
        else:
            user=df[(df["acc_num"] == acc_number) & (df["acc_pin"]==pi)]
            #if acc_number == acc_number and pin == pin:
            if not user.empty:
                st.session_state["logged_in"] = True
                balance = int(user.iloc[0]["initial_balance"])
                st.session_state["initial_balance"] = balance
                #st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials.")

    #st.caption(f"Demo credentials: account `{APP_ACCOUNT_NUMBER}`, pin `{APP_PIN}`")
    st.stop()


if st.session_state["account"] is None:
     
    st.subheader("🏦 Select account")
 
    st.session_state["account_type"] = st.selectbox(
        "Account type",
        options=["Savings", "Checking"],
        index=0 if st.session_state["account_type"] == "Savings" else 1,
    )
    st.write(f"Initial balance: **{st.session_state['initial_balance']}**")

    if st.button("Select"):
        if st.session_state["account_type"] == "Savings":
            st.session_state["account"] = SavingsAccount(st.session_state["initial_balance"])
        else:
            st.session_state["account"] = CheckingAccount(st.session_state["initial_balance"])
            # If we resumed a prior checking account, restore remaining overdraft.
            if "saved_overdraft_remaining" in st.session_state and st.session_state["saved_overdraft_remaining"] is not None:
                st.session_state["account"].overdraft_remaining = int(st.session_state["saved_overdraft_remaining"])
       
        st.rerun()

    st.stop()


account = st.session_state["account"]

st.subheader("Account")
balance_placeholder = st.empty()

if isinstance(account, CheckingAccount):
    st.caption(f"Overdraft limit: {account.overdraft_limit} | Overdraft fee: {account.overdraft_fee}")


tab_deposit, tab_withdraw, tab_balance = st.tabs(["Deposit", "Withdraw", "Balance"])

with tab_deposit:
    amount = st.number_input("Deposit amount", min_value=1, step=100, value=100)
    if st.button("Deposit"):
        st.session_state["last_message"] = account.deposit(int(amount))

with tab_withdraw:
    amount_w = st.number_input("Withdraw amount", min_value=1, step=100, value=100, key="withdraw_amount")

    confirm_overdraft = False
    if isinstance(account, CheckingAccount) and int(amount_w) > account.balance:
        st.warning("This withdrawal goes beyond your balance (overdraft).")
        confirm_overdraft = st.checkbox("Confirm overdraft + fee", value=False)

    if st.button("Withdraw"):
        if isinstance(account, CheckingAccount):
            st.session_state["last_message"] = account.withdraw(
                int(amount_w), confirm_overdraft=bool(confirm_overdraft)
            )
        else:
            # For savings accounts, keep withdrawals simple: no overdraft, no fees.
            if int(amount_w) > account.balance:
                st.session_state["last_message"] = "Insufficient funds: savings accounts cannot be overdrawn."
            else:
                st.session_state["last_message"] = account.withdraw(int(amount_w))
     

    if st.session_state["last_message"]:
        st.info(st.session_state["last_message"])

    
    

with tab_balance:
    st.write(f"Balance: **{account.balance}**")

balance_placeholder.metric("Current balance", account.balance)


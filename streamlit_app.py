import random

import streamlit as st

from ATM_BANKING import CheckingAccount, SavingsAccount


APP_ACCOUNT_NUMBER = 12345678
APP_PIN = 1234


def _init_state() -> None:
    st.session_state.setdefault("logged_in", False)
    st.session_state.setdefault("account", None)
    st.session_state.setdefault("account_type", "Savings")
    st.session_state.setdefault("initial_balance", random.randint(100, 10000))
    st.session_state.setdefault("last_message", "")


def _reset() -> None:
    for k in ["logged_in", "account", "account_type", "initial_balance", "last_message"]:
       if k in st.session_state:
           del st.session_state[k]
    st.rerun()


_init_state()

st.title("Universal Banking System")

with st.sidebar:
    st.subheader("Session")
    if st.session_state["logged_in"]:
        st.success("Logged in")
        if st.button("Reset / Logout"):
            _reset()
    else:
        st.info("Not logged in")


if not st.session_state["logged_in"]:
    st.subheader("Login")
    with st.form("login_form", clear_on_submit=False):
        acc_number_raw = st.text_input("Account number", value="")
        pin_raw = st.text_input("PIN", value="", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        try:
            acc_number = int(acc_number_raw.strip())
            pin = int(pin_raw.strip())
        except ValueError:
            st.error("Please enter numeric account number and PIN.")
        else:
            if acc_number == APP_ACCOUNT_NUMBER and pin == APP_PIN:
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Invalid credentials.")

    st.caption(f"Demo credentials: account `{APP_ACCOUNT_NUMBER}`, pin `{APP_PIN}`")
    st.stop()


if st.session_state["account"] is None:
    st.subheader("Create account")
    st.session_state["account_type"] = st.selectbox(
        "Account type",
        options=["Savings", "Checking"],
        index=0 if st.session_state["account_type"] == "Savings" else 1,
    )
    st.write(f"Initial balance: **{st.session_state['initial_balance']}**")

    if st.button("Create"):
        if st.session_state["account_type"] == "Savings":
            st.session_state["account"] = SavingsAccount(st.session_state["initial_balance"])
        else:
            st.session_state["account"] = CheckingAccount(st.session_state["initial_balance"])
        st.rerun()

    st.stop()


account = st.session_state["account"]

st.subheader("Account")
st.metric("Current balance", account.balance)

if isinstance(account, CheckingAccount):
    st.caption(f"Overdraft limit: {account.overdraft_limit} | Overdraft fee: {account.overdraft_fee}")


tab_deposit, tab_withdraw, tab_balance = st.tabs(["Deposit", "Withdraw", "Balance"])

with tab_deposit:
    amount = st.number_input("Deposit amount", min_value=1, step=100, value=100)
    if st.button("Deposit"):
        st.session_state["last_message"] = account.deposit(int(amount))
    if st.session_state["last_message"]:
        st.info(st.session_state["last_message"])

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
            st.session_state["last_message"] = account.withdraw(int(amount_w))

    if st.session_state["last_message"]:
        st.info(st.session_state["last_message"])

with tab_balance:
    st.write(f"Balance: **{account.balance}**")


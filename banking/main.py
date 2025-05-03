from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from banking.errors import AccountNotFoundError, InsufficientFundsError, NegativeAmountError
from banking.models import (
    Bank
)

app = FastAPI(title="Simple Banking API")
bank = Bank()


class AccountCreate(BaseModel):
    name: str
    initial_balance: float


class Transaction(BaseModel):
    name: str
    amount: float


class Transfer(BaseModel):
    sender: str
    recipient: str
    amount: float


@app.post("/accounts/")
def create_account(data: AccountCreate):
    try:
        account = bank.create_account(data.name, data.initial_balance)
        return {"message": f"Account '{account.name}' created."}
    except ValueError as e:
        raise HTTPException(400, str(e))


@app.get("/accounts/{name}")
def get_balance(name: str):
    try:
        account = bank.get_account(name)
        return {"name": account.name, "balance": account.balance}
    except AccountNotFoundError as e:
        raise HTTPException(404, str(e))


@app.post("/deposit")
def deposit(data: Transaction):
    try:
        account = bank.get_account(data.name)
        account.deposit(data.amount)
        return {"message": f"{data.amount:.2f} deposited to {data.name}"}
    except (AccountNotFoundError, NegativeAmountError) as e:
        raise HTTPException(400, str(e))


@app.post("/withdraw")
def withdraw(data: Transaction):
    try:
        account = bank.get_account(data.name)
        account.withdraw(data.amount)
        return {"message": f"{data.amount:.2f} withdrawn from {data.name}"}
    except (AccountNotFoundError, NegativeAmountError, InsufficientFundsError) as e:
        raise HTTPException(400, str(e))


@app.post("/transfer")
def transfer(data: Transfer):
    try:
        sender = bank.get_account(data.sender)
        recipient = bank.get_account(data.recipient)
        sender.transfer(recipient, data.amount)
        return {"message": f"{data.amount:.2f} transferred from {data.sender} to {data.recipient}"}
    except (AccountNotFoundError, NegativeAmountError, InsufficientFundsError, ValueError) as e:
        raise HTTPException(400, str(e))

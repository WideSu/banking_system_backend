from fastapi import FastAPI, HTTPException
import os
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


class TransactionAmount(BaseModel):
    amount: float


class Transfer(BaseModel):
    sender: str
    recipient: str
    amount: float


@app.post("/accounts/")
async def create_account(data: AccountCreate):
    try:
        account = bank.create_account(data.name, data.initial_balance)
        return {"message": f"Account '{account.name}' created."}
    except ValueError as e:
        raise HTTPException(400, str(e))


@app.get("/accounts/{name}")
async def get_balance(name: str):
    try:
        account = bank.get_account(name)
        return {"name": account.name, "balance": account.balance}
    except AccountNotFoundError as e:
        raise HTTPException(404, str(e))


@app.post("/accounts/{name}/deposits")
async def deposit(name: str, data: TransactionAmount):
    try:
        account = bank.get_account(name)
        account.deposit(data.amount)
        return {"message": f"{data.amount:.2f} deposited to {name}"}
    except (AccountNotFoundError, NegativeAmountError) as e:
        raise HTTPException(400, str(e))


@app.post("/accounts/{name}/withdrawals")
async def withdraw(name: str, data: TransactionAmount):
    try:
        account = bank.get_account(name)
        account.withdraw(data.amount)
        return {"message": f"{data.amount:.2f} withdrawn from {name}"}
    except (AccountNotFoundError, NegativeAmountError, InsufficientFundsError) as e:
        raise HTTPException(400, str(e))


@app.post("/transfers")
async def transfer(data: Transfer):
    try:
        sender = bank.get_account(data.sender)
        recipient = bank.get_account(data.recipient)
        sender.transfer(recipient, data.amount)
        return {"message": f"{data.amount:.2f} transferred from {data.sender} to {data.recipient}"}
    except (AccountNotFoundError, NegativeAmountError, InsufficientFundsError, ValueError) as e:
        raise HTTPException(400, str(e))


if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)

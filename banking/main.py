from fastapi import FastAPI, HTTPException
import os
from contextlib import asynccontextmanager
from pydantic import BaseModel
from banking.errors import AccountNotFoundError, InsufficientFundsError, NegativeAmountError
from banking.database import Database

db = Database()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize DB
    await db.init_db()
    yield
    # Shutdown: (Optional cleanup)

app = FastAPI(title="Simple Banking API", lifespan=lifespan)


class AccountCreate(BaseModel):
    name: str
    initial_balance: float


class TransactionAmount(BaseModel):
    amount: float


class Transfer(BaseModel):
    sender: str
    recipient: str
    amount: float


@app.get("/")
async def root():
    return {"message": "Welcome to the Simple Banking API"}


@app.post("/accounts/")
async def create_account(data: AccountCreate):
    try:
        await db.create_account(data.name, data.initial_balance)
        return {"message": f"Account '{data.name}' created."}
    except ValueError as e:
        raise HTTPException(400, str(e))


@app.get("/accounts/{name}")
async def get_balance(name: str):
    try:
        balance = await db.get_balance(name)
        return {"name": name, "balance": balance}
    except AccountNotFoundError as e:
        raise HTTPException(404, str(e))


@app.post("/accounts/{name}/deposits")
async def deposit(name: str, data: TransactionAmount):
    try:
        await db.deposit(name, data.amount)
        return {"message": f"{data.amount:.2f} deposited to {name}"}
    except (AccountNotFoundError, NegativeAmountError) as e:
        raise HTTPException(400, str(e))


@app.post("/accounts/{name}/withdrawals")
async def withdraw(name: str, data: TransactionAmount):
    try:
        await db.withdraw(name, data.amount)
        return {"message": f"{data.amount:.2f} withdrawn from {name}"}
    except (AccountNotFoundError, NegativeAmountError, InsufficientFundsError) as e:
        raise HTTPException(400, str(e))


@app.post("/transfers")
async def transfer(data: Transfer):
    try:
        await db.transfer(data.sender, data.recipient, data.amount)
        return {"message": f"{data.amount:.2f} transferred from {data.sender} to {data.recipient}"}
    except (AccountNotFoundError, NegativeAmountError, InsufficientFundsError, ValueError) as e:
        raise HTTPException(400, str(e))


if __name__ == "__main__":  # pragma: no cover
    import uvicorn
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)

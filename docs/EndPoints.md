## Endpoints
You can also view the automatically generated API docs by FastAPI via http://localhost:8000/docs#/

<img src="img/endpoints.jpg" alt="Endpoints Documentation" style="width:100%;">

### Create Account
#### POST `/accounts`
Create a new bank account.
#### Request Body (JSON)
```json
{
  "name": "Alice",
  "initial_balance": 100.0
}
```
####  Response (200 OK)
```json
{
  "message": "Account created for Alice with balance 100.0"
}
```
### Response (400 Bad Request)
```json
{
  "detail": "Initial balance cannot be negative"
}
```
### Get Account Balance
#### GET `/accounts/{name}/balance`
Retrieve the current balance of an account.
#### Response (200 OK):
```json
{
  "name": "Alice",
  "balance": 100.0
}
```
#### Response (404 Not Found)
```json
{
  "detail": "Account 'Alice' not found"
}
```
### Deposit
#### POST `/accounts/{name}/deposit`
Add money to an account.
#### Request Body
```json
{
  "amount": 50.0
}
```
#### Response (200 OK)
```json
{
  "message": "Deposited 50.0 to Alice. New balance: 150.0"
}
```
#### Response (400 Bad Request)
```json
{
  "detail": "Amount must be positive"
}
```
### Withdraw
#### POST `/accounts/{name}/withdraw`
Withdraw money from an account.
#### Request Body
```json
{
  "amount": 30.0
}
```
#### Response (200 OK)
```json
{
  "message": "Withdrew 30.0 from Alice. New balance: 120.0"
}
```
#### Response (400 Bad Request or 403 Forbidden)
```json
{
  "detail": "Cannot withdraw 500.0; balance is only 100.0"
}
```
### Transfer
#### POST `/accounts/{from_name}/transfer/{to_name}`
Transfer money between accounts.
#### Request Body
```json
{
  "amount": 25.0
}
```
### Response (200 OK)
```json
{
  "message": "Transferred 25.0 from Alice to Bob"
}
```
### Response (400 or 403 Error)
```json
{
  "detail": "Cannot transfer to the same account" // or insufficient funds
}
```
### Transaction History
#### GET `/accounts/{name}/history`
Retrieve transaction history.
#### Response (200 OK)
```json
{
  "name": "Alice",
  "transactions": [
    "Account created with balance: 100.00",
    "Deposited: 50.00",
    "Withdrawn: 30.00",
    "Transferred to: 25.00 Bob"
  ]
}
```

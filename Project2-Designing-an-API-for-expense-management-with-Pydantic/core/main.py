from fastapi import FastAPI, HTTPException, status
from typing import Dict, List, Optional, Any, Union
from schemas import ExpenseSchema, ExpenseCreate, ExpenseUpdate, ExpenseUpdatePartial, ExpenseDelete

app = FastAPI(title="Project 1 - Expense Management API")

expenses_db: Dict[int, ExpenseSchema] = {
    1: ExpenseSchema(description="Food", amount=50),
    2: ExpenseSchema(description="Transportation", amount=200),
    3: ExpenseSchema(description="Entertainment", amount=100),
}

@app.get("/get_all_expenses", status_code=status.HTTP_200_OK)
def get_all_expenses() -> Dict[int, ExpenseSchema]:
    if expenses_db:
        return expenses_db
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No expenses found...")


@app.get("/get_expense/{expense_id}", status_code=status.HTTP_200_OK)
def get_expense(expense_id:int) -> ExpenseSchema:
    if expense_id in expenses_db.keys():
        return expenses_db[expense_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found...")


@app.post("/add_expense/{expense_id}", status_code=status.HTTP_201_CREATED)
def add_expense(expense: ExpenseCreate) -> Dict[str, str]:
    if expense.id in expenses_db.keys():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Expense already exists...")
    else:
        expenses_db[expense.id] = ExpenseSchema(
            description=expense.description,
            amount=expense.amount
        )
        return {"detail": "Expense added successfully..."}


@app.put("/update_expense/{expense_id}", status_code=status.HTTP_200_OK)
def update_expense(expense: ExpenseUpdate) -> Dict[str, str]:
    if expense.id in expenses_db.keys():
        expenses_db[expense.id] = ExpenseSchema(
            description=expense.description,
            amount=expense.amount
        )
        return {"detail": "Expense updated successfully..."}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found...")


@app.patch("/update_expense_partial/{expense_id}", status_code=status.HTTP_200_OK)
def update_expense_partial(expense: ExpenseUpdatePartial) -> Dict[str, str]:
    if expense.id in expenses_db.keys():
        if expense.description:
            expenses_db[expense.id].description = expense.description
        if expense.amount:
            expenses_db[expense.id].amount = expense.amount
        return {"detail": "Expense updated successfully..."}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found...")


@app.delete("/delete_expense/{expense_id}")
def delete_expense(expense: ExpenseDelete) -> Dict[str, str]:
    if expense.id in expenses_db.keys():
        expenses_db.pop(expense.id)
        return {"detail": "Expense deleted successfully..."}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found...")

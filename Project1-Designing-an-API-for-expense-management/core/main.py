from fastapi import FastAPI, HTTPException, status
from typing import Dict, List, Optional, Any, Union

app = FastAPI(title="Project 1 - Expense Management API")

expenses_db: Dict[int, Dict[str, Any]] = {
    1: {
        "description": "Food",
        "amount": 100,
    }
}

@app.get("/get_all_expenses", status_code=status.HTTP_200_OK)
def get_all_expenses() -> Dict[int, Dict[str, Any]]:
    if expenses_db:
        return expenses_db
    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No expenses found...")

@app.get("/get_expense/{expense_id}", status_code=status.HTTP_200_OK)
def get_expense(expense_id:int) -> Dict[str, Any]:
    if expense_id in expenses_db.keys():
        return expenses_db.get(expense_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found...")

@app.post("/add_expense/{expense_id}", status_code=status.HTTP_201_CREATED)
def add_expense(expense_id:int, description:str, amount:int) -> Dict[str, str]:
    if expense_id in expenses_db.keys():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Expense already exists...")
    else:
        expenses_db[expense_id] = {
            "description": description,
            "amount": amount
        }
        return {"detail": "Expense added successfully..."}

@app.put("/update_expense/{expense_id}", status_code=status.HTTP_200_OK)
def update_expense(expense_id:int, description:str, amount:int) -> Dict[str, str]:
    if expense_id in expenses_db.keys():
        expenses_db[expense_id] = {
            "description": description,
            "amount": amount
        }
        return {"detail": "Expense updated successfully..."}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found...")

@app.patch("/update_expense_partial/{expense_id}", status_code=status.HTTP_200_OK)
def update_expense_partial(expense_id:int, description:Optional[str]=None, amount:Optional[int]=None) -> Dict[str, str]:
    if expense_id in expenses_db.keys():
        if description:
            expenses_db[expense_id]["description"] = description
        if amount:
            expenses_db[expense_id]["amount"] = amount
        return {"detail": "Expense updated successfully..."}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found...")

@app.delete("/delete_expense/{expense_id}")
def delete_expense(expense_id:int) -> Dict[str, str]:
    if expense_id in expenses_db.keys():
        expenses_db.pop(expense_id)
        return {"detail": "Expense deleted successfully..."}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found...")
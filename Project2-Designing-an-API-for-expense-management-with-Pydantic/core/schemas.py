from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Dict


class ExpenseSchema(BaseModel):
    description: str = Field(
        min_length=1,
        max_length=500,
        description="Description of the expense",
        examples=["Food", "Transportation", "Entertainment"]
    )
    amount: float = Field(
        gt=0,
        description="Amount of the expense",
        examples=[100.50, 250.00, 75.25]
    )

class ExpenseCreate(ExpenseSchema):
    id: int = Field()

class ExpenseUpdate(ExpenseSchema):
    id: int = Field(
        gt=0,
        description="Unique identifier for the expense",
        examples=[1, 2, 3]
    )

class ExpenseUpdatePartial(ExpenseSchema):
    id: int = Field(
        gt=0,
        description="Unique identifier for the expense",
        examples=[1, 2, 3]
    )
    description: Optional[str] = Field(
        None,
        min_length=1,
        max_length=500,
        description="Updated description of the expense",
        examples=["Updated Food Expense"]
    )
    amount: Optional[float] = Field(
        None,
        gt=0,
        description="Updated amount of the expense (must be greater than 0)",
        examples=[150.75]
    )

class ExpenseDelete(BaseModel):
    id: int = Field(
        gt=0,
        description="Unique identifier for the expense",
        examples=[1, 2, 3]
    )

class ResponseMessage(BaseModel):
    detail: str = Field(
        description="Response message",
        examples=["Expense added successfully...", "Expense updated successfully...", "Expense deleted successfully..."]
    )

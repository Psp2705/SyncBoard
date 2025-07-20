from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class TaskSchema(BaseModel):
    item: str = Field(..., example="Complete project documentation", description="The title of the task")
    description: Optional[str] = Field(None, example="write and review API docs", description="Detailed description of the task")
    assignee: Optional[str] = Field(None, example="Ayesha Ankush Aditi", description="Person assigned to the task")
    priority: Optional[str] = Field("medium", example="medium", description="Priority of the task: low, medium, high")
    status: Optional[str] = Field("pending", example="pending", description="Task status: pending, in_progress, completed")
    due_date: Optional[datetime] = Field(None, example="2025-07-30T12:00:00", description="Task due date")
    created_at: datetime = Field(default_factory=datetime.now(), description="Timestamp when task was created")
    updated_at: Optional[datetime] = Field(None, description="Timestamp when task was last updated")


    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Complete project documentation",
                "description": "Write and review API docs",
                "assignee": "Aditi",
                "priority": "high",
                "status": "pending",
                "due_date": "2025-07-30T12:00:00",
            }
        }
    )

class UpdateTaskSchema(BaseModel):
    title: Optional[str] = Field(None, example="Update project documentation", description="Updated task title")
    description: Optional[str] = Field(None, example="update and review API docs", description="Updated task description")
    assignee: Optional[str] = Field(None, example="John Doe", description="Updated task assignee")
    priority: Optional[str] = Field(None, example="high", description="Updated priority: low, medium, high")
    status: Optional[str] = Field(None, example="in_progress", description="Updated status: pending, in_progress, completed")
    due_date: Optional[datetime] = Field(None, example="2025-07-30T12:00", description="Updated due date")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Update project documentation",
                "description": "Revised API docs with examples",
                "assignee": "John Doe",
                "priority": "high",
                "status": "in_progress",
                "due_date": "2025-08-01T12:00:00"
                            
            }
        }
    )
                                  

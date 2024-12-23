from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/all_tasks")
async def all_tasks():
    pass

@router.get("/{task_id}")
async def task_by_id(task_id: int):
    pass

@router.post("/create")
async def creaty_task():
    pass

@router.put("/update_task")
async def update_task():
    pass

@router.delete("/delete")
async def delete_task():
    pass

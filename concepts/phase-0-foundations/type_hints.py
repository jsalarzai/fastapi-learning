def describe_task(title: str, priority: int, done: bool) -> str:
    status = "complete" if done else "pending"
    return f"Task: {title} | Priority: {priority} | Status: {status}"


print(describe_task("Buy groceries", 2, False))

print(describe_task(123, "high", False))
print(describe_task("Buy groceries", 2, "no"))

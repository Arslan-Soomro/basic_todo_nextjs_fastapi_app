export async function getTodos() {
    const response = await fetch("/api/todos");
    const data = await response.json();
    return data;
}

export async function createTodo(todo) {
    const response = await fetch("/api/todos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(todo),
    });
    const data = await response.json();
    return data;
}

export async function deleteTodo(todoId) {
    const response = await fetch(`/api/todos/${todoId}`, {
        method: "DELETE",
    });
    const data = await response.json();
    return data;
}
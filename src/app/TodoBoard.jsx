"use client";

import { getTodos, createTodo, deleteTodo } from "@/utils/utils";
import { useEffect, useState } from "react";

export default function TodoBoard() {
  const [todos, setTodos] = useState([]);
  const [todoTitle, setTodoTitle] = useState("");

  useEffect(() => {
    getTodos().then((data) => {
      setTodos(data);
    });
  }, []);

  async function handleAddTodo() {
    const newTodo = await createTodo({
      title: todoTitle,
    });
    setTodos([...todos, newTodo]);
    setTodoTitle("");
    console.log("New Todo: ", newTodo);
  }

  async function handleDeleteTodo(todoId) {
    await deleteTodo(todoId);

    const newTodos = todos.filter((todo) => todo.id !== todoId);
    setTodos(newTodos);
  }

  return (
    <main className="bg-white h-screen w-screen flex items-center justify-center text-black">
      <div className="flex flex-col gap-2">
        <div className="flex gap-2">
          <input
            className="border border-black rounded-md text-sm p-2"
            placeholder="What do you want to do ?"
            value={todoTitle}
            onChange={(e) => setTodoTitle(e.target.value)}
          />
          <button className="bg-blue-500 text-white px-2 py-1 rounded-md" onClick={handleAddTodo}>
            Add Todo
          </button>
        </div>
        <ul className="flex flex-col gap-2">
          {todos?.map((todo) => {
            return (
              <li
                key={todo.id}
                className="flex justify-between items-center border-b border-gray-300 p-2"
              >
                <span> {todo.id} - </span>
                <span>{todo.title}</span>
                <button onClick={() => deleteTodo(todo.id)} className="bg-red-500 text-white text-sm px-2 py-1 rounded-md">
                  Delete
                </button>
              </li>
            );
          })}
        </ul>
      </div>
    </main>
  );
}

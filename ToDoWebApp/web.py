import  streamlit as st
import functions


st.title("My Todo App")
st.subheader("There are My Todos")

todos = functions.get_todos()

def add_todo():
    new_todo_text = st.session_state["new_todo"].strip()

    if new_todo_text != "":
        todo = st.session_state["new_todo"] + "\n"
        todos.append(todo)
        functions.write_todos(todos)


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", on_change=add_todo, key="new_todo",
              placeholder="Add new todo")
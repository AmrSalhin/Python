import  streamlit as st
from streamlit import checkbox

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


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", on_change=add_todo, key="new_todo",
              placeholder="Add new todo")
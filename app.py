import streamlit as st
from seed import seed_tasks

st.set_page_config(page_title="Todo App", layout="wide")

st.title("📝 Todo App")

# Initialize session state with seed tasks on first run
if "todos" not in st.session_state:
    st.session_state.todos = seed_tasks()

# Input section
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
with col1:
    new_task = st.text_input("Ajouter une tâche:", placeholder="Votre tâche ici")
with col2:
    new_project = st.text_input("Projet", placeholder="CORMA", key="proj_input")
with col3:
    new_section = st.text_input("Section", placeholder="Site + offre", key="sec_input")
with col4:
    if st.button("Ajouter", use_container_width=True):
        if new_task.strip():
            st.session_state.todos.append({
                "id": f"task_{len(st.session_state.todos)}",
                "task": new_task,
                "project": new_project or "Général",
                "section": new_section or "À faire",
                "completed": False,
                "priority": "Moyenne",
                "impact": 3,
                "effort": 3,
                "status": "Todo",
                "due": None,
                "tags": [],
            })
            st.rerun()

# Display todos
st.subheader("Vos Tâches")
if st.session_state.todos:
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        search = st.text_input("Rechercher", placeholder="Filtrer par texte...")
    with col2:
        filter_project = st.multiselect("Projets", 
                                       sorted(set(t.get("project", "Général") for t in st.session_state.todos)),
                                       default=None)
    
    # Filter todos
    filtered_todos = st.session_state.todos
    if search:
        filtered_todos = [t for t in filtered_todos if search.lower() in t.get("task", "").lower()]
    if filter_project:
        filtered_todos = [t for t in filtered_todos if t.get("project") in filter_project]
    
    for i, todo in enumerate(st.session_state.todos):
        if filtered_todos and todo not in filtered_todos:
            continue
        col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
        with col1:
            completed = st.checkbox(f"{todo.get('task', '')} ({todo.get('project', '')})", 
                                   value=todo["completed"], 
                                   key=f"todo_{i}_{todo.get('id', i)}")
            st.session_state.todos[i]["completed"] = completed
        with col2:
            st.caption(f"Priorité: {todo.get('priority', 'N/A')}")
        with col3:
            st.caption(f"Impact: {todo.get('impact', 3)}")
        with col4:
            st.caption(f"Effort: {todo.get('effort', 3)}")
        with col5:
            if st.button("Supprimer", key=f"delete_{i}_{todo.get('id', i)}"):
                st.session_state.todos.pop(i)
                st.rerun()
else:
    st.info("Aucune tâche. Ajoutez-en une pour commencer!")

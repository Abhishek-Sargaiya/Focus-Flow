import React from 'react'
import {TodoItem} from './TodoItem'
const Todos = (props) => {
  return (
    <div className='container my-3' >
      <h3 className='container my-3'>Todos List</h3>
      {props.todos.length === 0 ? "No Todos to Display" : props.todos.map((todo)=>{
        return (
        <>
        <TodoItem todo = {todo} key={todo.sno} onDelete={props.onDelete}/>
        <hr />  
        </>
        )
      })}
    </div>
  )
}

export default Todos;

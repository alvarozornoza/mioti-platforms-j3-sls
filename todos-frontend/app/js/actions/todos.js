import 'whatwg-fetch';

import { API_URL } from './index';

import {
  ERROR,
  CREATE_TODO,
  GET_TODOS,
  GET_TODO,
  UPDATE_TODO,
  DELETE_TODO
} from './constants';

export function createTodo(todo) {
  return (dispatch) => fetch(`${API_URL}`, {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify(todo)
  })
  .then(response => response.json())
  .then(json => dispatch({
    type: CREATE_TODO,
    payload: json
  }))
  .catch(exception => dispatch({
    type: ERROR,
    payload: exception.message
  }));
}

export function getTodos() {
  return (dispatch) => fetch(`${API_URL}`, {
    method: 'GET'
  })
  .then(response => response.json())
  .then(json => dispatch({
    type: GET_TODOS,
    payload: json
  }))
  .catch(exception => dispatch({
    type: ERROR,
    payload: exception.message
  }));
}

export function getTodo(todo) {
  return (dispatch) => fetch(`${API_URL}/${todo.id}`, {
    method: 'GET'
  })
  .then(response => response.json())
  .then(json => dispatch({
    type: GET_TODO,
    payload: json
  }))
  .catch(exception => dispatch({
    type: ERROR,
    payload: exception.message
  }));
}

export function updateTodo(todo) {
  return (dispatch) => fetch(`${API_URL}/${todo.id}`, {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'PUT',
    body: JSON.stringify(todo.body)
  })
  .then(response => response.json())
  .then(json => dispatch({
    type: UPDATE_TODO,
    payload: json
  }))
  .catch(exception => dispatch({
    type: ERROR,
    payload: exception.message
  }));
}

export function deleteTodo(id) {
  return (dispatch) => fetch(`${API_URL}/${id}`, {
    method: 'DELETE'
  })
  .then(response => response.json())
  .then(json => dispatch({
    type: DELETE_TODO,
    payload: json
  }))
  .catch(exception => dispatch({
    type: ERROR,
    payload: exception.message
  }));
}

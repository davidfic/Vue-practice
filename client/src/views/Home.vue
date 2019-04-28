<template>
  <div id="app">
    <div class="container">


    </div>
    <!-- <AddTodo v-on:add-todo="addTodo"/> -->
    <!-- <Todos v-bind:todos="todos" v-on:del-todo="deleteTodo"/> -->
    <Buckets v-bind:buckets="buckets" v-on:add-money="addMoney"/>
    
    
  </div>
</template>

<script>

import Header from '../components/layout/Header'; 
import Todos from '../components/Todos'; 
import AddTodo from '../components/AddTodo'; 
import Buckets from '../components/Buckets';
import Chores from '../components/Chores'

import axios from 'axios';

export default {
  name: 'Home',
  components: {
    Header,
    Todos,
    AddTodo,
    Buckets,
  },
  data() {
    return {
      buckets: [
        {
          id: 1,
          name: 'spend',
          amount: 101,
        },
        {
          id: 2,
          name: 'save',
          amount: 100,
        },
        {
          id: 3,
          name: 'share',
          amount: 100,
        },
      ],
      todos: []
    }
  },
  methods: {
    deleteTodo(id) {
      this.todos = this.todos.filter(todo => todo.id !== id)
    },
    addTodo(newTodo) {
      this.todos = [...this.todos, newTodo]
    },
    addMoney(id, amount) {
      //update amount in bucket with new amount adeded
      console.log('going to add ' +amount + ' to bucket with id ' + id ) 
             
    },
  },
  created() {
    axios.get('http://localhost:5000/todos')
      .then(res => this.todos = res.data)
      .catch(err => console.log(err));
  }
}
</script>

<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.4;
  }

  /* .container {
    max-width: 1100px;
    margin: auto;
    overflow: auto;
    padding: 0 2rem;
  } */
  .btn {
    display: inline-block;
    border: none;
    background: #555;
    color: #fff;
    padding: 7px 20px;
    cursor: pointer;
  }

  .btn:hover {
    background: #666;
  }
</style>

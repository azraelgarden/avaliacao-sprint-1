<template>
  <div class='container'>
    <input type="text" v-model="username" >
    <button @click="submit">search</button>
    <p>username:{{result.login}}</p>
    <p>Name:{{result.name}}</p>
    <p>Public Repos:{{result['public_repos']}}</p>

  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    methods: {
      submit() {
        const api = axios.create({baseURL:'http://localhost:3000'})
        api.get(this.username).then((result)=>{
          console.log(result)
          this.result = result.data
        }).catch(console.log)
      }
    },
    data() {
      return {
        username: '',
        result: ''
      }
    } 
  }
</script>

<style scoped>
  .container {   
    height: 100vh;
  }
</style>

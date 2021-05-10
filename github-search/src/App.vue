<template>
  <div class='container'>
    <input type="text" v-model="username" >
    <button @click="submit">search</button>
    <p>{{result}}</p>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    methods: {
      submit() {
        console.log(this.text)
        const api = axios.create({baseURL:'http://localhost:3000'})
        api.get(this.username).then((result)=>{
          this.result = JSON.stringify(result)
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

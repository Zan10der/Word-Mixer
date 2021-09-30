<template>
  <Scrabble/>
</template>

<script>
import Scrabble from './components/Scrabble.vue'

export default {
  name: 'App',
  
  components: {
    Scrabble,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>


<!--- Original Code
<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <div id="app">
    {{ sentences }}
  </div>
</template>

<script>
import axios from 'axios'
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data: () => ({
    sentences: []
  }),

  components: {
    HelloWorld,
  },

  mounted () {
    axios.get('http://127.0.0.1:8000/api/scrabble/').then((response) => {
      this.sentences = response.data
    })
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
--->
<template>
  <div id="app">
  <home @func="getmsgfromson"/>
  </div> 
</template>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  width: 100%;
}
</style>
<script>
import home from './components/home.vue'
export default {
  name: 'App',
  components: {
    home
  }
}
</script>

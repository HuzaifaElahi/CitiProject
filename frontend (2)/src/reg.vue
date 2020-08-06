<template>
  <div id="reg">
  <register @func="getmsgfromson"/>
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
import register from './components/register.vue'
export default {
  name: 'reg',
  components: {
    register
  }
}
</script>

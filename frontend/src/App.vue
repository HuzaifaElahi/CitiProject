<template>
  <div id="app">
  <nav>
      <router-link to="/"></router-link>
      <router-link to="/about"></router-link>
  
  </nav>
  <router-view style="height:100%"></router-view>
  </div>
</template>

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
}

</style>
<script>
export default {
  name: 'app',
 
}
  </script>


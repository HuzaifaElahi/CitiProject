<template>
  <div id="app">

  <a-layout id="components-layout-demo-top" class="layout">
    <a-layout-header style="text-align: right">
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="horizontal"
        :default-selected-keys="['register']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="login">
          Login
        </a-menu-item>
        <a-menu-item key="register">
          Register
        </a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="padding: 50px 50px">
      <div class="flexbox" :style="{ background: '#fff', padding: '24px', minHeight: '280px'}">
        <antdform />
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      Ant Design ©2018 Created by Ant UED
    </a-layout-footer>
  </a-layout>
  </div>
</template>

<style>
#components-layout-demo-top .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 24px 16px 0;
  float: left;
}
#components-layout-demo-top {
  height: 100%;
  width: 100%;
  text-align: center;

}
.flexbox {
  display: flex;
  height: 100%;
  justify-content: center;
}

</style>

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
</style><script>
import antdform from './components/form.vue'

export default {
  name: 'App',
  components: {
    antdform
  }
}
</script>

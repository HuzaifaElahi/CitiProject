<template>
   <div class="layout">
<!--  <a-layout id="components-layout-demo-top" class="layout">
   <a-layout-header class="header" style="padding: 24px"> -->
 <a-row type="flex" class="grid">
      <a-col style="background-color:white;" :flex="1">
        <div style="padding: 24px;text-align:center;"><img style="height:auto; width: 80px" :src="imgUrl"> </div>
     <!-- <a-menu style="text-align: right" class="menu"
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
      </a-menu> -->
      <br>
      <br>
      <div style = "text-align: center; padding: 32px;">
      <a-button type="primary" size="large" block>
        Login
      </a-button>
      <br>
      <br>
      <a-button type="primary" size="large" block>
        Register
      </a-button>
      </div>
    </a-col>
  <!--  </a-layout-header> -->
   <!-- <a-layout-content style="padding: 150px 50px">
      <div class="flexbox" :style="{padding: '24px', minHeight: '280px'}">
        <antdform class="antd-form"/>
      </div>
    </a-layout-content>
    <a-layout-footer class="footer">
    </a-layout-footer>-->
    <a-col :flex="6" class="content">
    <div class="flexbox" :style="{ padding: '24px', minHeight: '280px'}">
        <antdform class="antd-form"/>
      </div>
    </a-col>
    </a-row>
 <!-- </a-layout>-->
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
.layout {
  height: 100%;
  width: 100%;
}
.flexbox {
  display: flex;
  height: 100%;
  justify-content:center;
}
.menu, .layout, .header, .footer {
    background-color: #1890ff;
    border-color: #1890ff;
    //font-family: 'Helvetica Neue';
    font-size: 30px;
    
}
.content {
  padding: 200px;
}
.grid {
  height: 100%;
}
.sidebar {
  backgroud-color:white;
  z-index: 1;
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
</style>



<script>
import antdform from './form.vue'
export default {
  name: 'register',
  components: {
    antdform
  },
  data() {
    return {
        imgUrl:"../assets/citilogo.png "
     }
  },

  created() {
    let urlTemp = "assets/citilogo.png";
    this.imgUrl = require("@/" + urlTemp);
  }
}
  </script>
  
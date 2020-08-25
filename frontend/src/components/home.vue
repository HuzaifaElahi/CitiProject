<template>
  <div class="layout">
    <a-row type="flex" class="grid">
      <a-col  :flex="2">
        <div style="padding: 24px;text-align:left;"><img style="height:auto; width: 80px" :src="imgUrl"> </div>
        <div style=" text-align: center; padding: 500px 200px;">
          <span style=" color: white; font-size:40px;">Welcome to CitiInvest!</span>
          <br>
          <h4 style=" color: white;">Get started in stocks, hassle free.</h4>
        </div>

    </a-col>
    <a-col style="background-color:white;text-align: center; padding: 500px 200px;" :flex="3" class="content">
    <div class="flexbox" style="background-color:white;"  :style="{ padding: '24px', minHeight: '280px'}">
      <a-form
    id="components-form-demo-normal-login"
    :form="form"
    class="login-form"
    @submit="handleSubmit"
  >
    <a-form-item>
      <a-input style="width: 100%;"
        
        placeholder="Username"
      >
        <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item>
      <a-input
       
        type="password"
        placeholder="Password"
      >
        <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item>
      <a-checkbox style="text-align: left;"
        v-decorator="[
          'remember',
          {
            valuePropName: 'checked',
            initialValue: true,
          },
        ]"
      >
        Remember me
      </a-checkbox>
      <a class="login-form-forgot" href="">
        Forgot password
      </a>
      <a-row type="flex" class="grid">
      <a-col  :flex="2">
      <a-button html-type="submit" class="login-form-button">
        Log in
        <!--<router-link to="/reg">Register</router-link>-->
      </a-button>
      </a-col>
      <a-col :flex="1"></a-col>
      <a-col  :flex="2">
      <a-button html-type="submit" class="login-form-button">
      <nav>
        <router-link to="/reg">Register</router-link>
      </nav>
  <router-view></router-view>
      </a-button>
      </a-col>
      </a-row>
    </a-form-item>
  </a-form>
      </div>
    </a-col>
    </a-row>
 <!-- </a-layout>-->
 </div>
</template>



<style>

.layout {
  height: 100%;
  width: 100%;
}
.flexbox {
  display: flex;
  height: 100%;
  justify-content:center;
  background-color: #0050b3;
}
.layout {
    background-color: #0050b3;
    //font-family: 'Helvetica Neue';
    font-size: 30px;
    
}
.content {
  background-color: #0050b3;
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
#components-form-demo-normal-login .login-form {
    width: 300px;
}
#components-form-demo-normal-login .login-form-forgot {
  float: right;
}
#components-form-demo-normal-login .login-form-button {
  width: 100%;
}
.ant-col.ant-form-item-control-wrapper {
    width: 100%;
}
#components-form-demo-normal-login .login-form.ant-form.ant-form-horizontal {
  min-width: 300px;
}
</style>


<script>
export default {
  name: 'home',

  data() {
    return {
        imgUrl:"../assets/citilogo.png "
     }
  },

  created() {
    let urlTemp = "assets/citilogo.png";
    this.imgUrl = require("@/" + urlTemp);
  },    
  
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: 'normal_login' });
    },
    methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log('Received values of form: ', values);
        }
      });
    },
  }
}
  </script>
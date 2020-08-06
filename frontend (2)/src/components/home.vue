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
        v-decorator="[
          'userName',
          { rules: [{ required: true, message: 'Please input your username!' }] },
        ]"
        placeholder="Username"
      >
        <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)" />
      </a-input>
    </a-form-item>
    <a-form-item>
      <a-input
        v-decorator="[
          'password',
          { rules: [{ required: true, message: 'Please input your Password!' }] },
        ]"
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
      <a-button @click="jump" type="primary" html-type="submit" class="login-form-button">
        Log in
      </a-button>
      </a-col>
      <a-col :flex="1"></a-col>
      <a-col  :flex="2">
      <a-button type="primary" html-type="submit" class="login-form-button">
        Register
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
}
.layout {
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
import loginform from './loginform.vue'
export default {
  name: 'home',
  components: {
    loginform
  },
  data() {
    return {
        imgUrl:"../assets/citilogo.png "
     }
  },

  created() {
    let urlTemp = "assets/citilogo.png";
    this.imgUrl = require("@/" + urlTemp);
  }，     
  
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: 'normal_login' });
    },
    methods: {
      jump() {
        this.$router.push({path: ''})
      },
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log('Received values of form: ', values);
        }
      });
    },
  },
}
  </script>
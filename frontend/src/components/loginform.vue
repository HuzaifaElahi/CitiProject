<template>
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
</template>

<script>
export default {
    name: 'loginform',
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
  },
};
</script>
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
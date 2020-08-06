<template>
  <a-form :form="form" @submit="handleSubmit">
    <a-form-item v-bind="formItemLayout">
    <span style="color:white; font-size:16px;font-family: 'Helvetica Neue';"  slot="label">E-mail</span>
      <a-input class="inputlabel"
        v-decorator="[
          'email',
          {
            rules: [
              {
                type: 'email',
                message: 'The input is not valid E-mail!',
              },
              {
                required: true,
                message: 'Please input your E-mail!',
              },
            ],
          },
        ]"
      />
    </a-form-item>
    <a-form-item v-bind="formItemLayout" has-feedback>
    <span style="color:white; font-size:16px;font-family: 'Helvetica Neue';" slot="label">
      Password&nbsp;
        <a-tooltip title="At least 8 characters">
          <a-icon type="question-circle-o" />
        </a-tooltip>
    </span>
      <a-input
        v-decorator="[
          'password',
          {
            rules: [
              {
                required: true,
                message: 'Please input your password!',
              },
              {
                validator: validateToNextPassword,
              },
            ],
          },
        ]"
        type="password"
      />
    </a-form-item>
    <a-form-item v-bind="formItemLayout" has-feedback>
    <span style="color:white; font-size:16px;font-family: 'Helvetica Neue';" slot="label">Confirm Password</span>
      <a-input
        v-decorator="[
          'confirm',
          {
            rules: [
              {
                required: true,
                message: 'Please confirm your password!',
              },
              {
                validator: compareToFirstPassword,
              },
            ],
          },
        ]"
        type="password"
        @blur="handleConfirmBlur"
      />
    </a-form-item>
    <a-form-item v-bind="formItemLayout">
      <span style="color:white; font-size:16px;font-family: 'Helvetica Neue';" slot="label">
        Username
      </span>
      <a-input
        v-decorator="[
          'Username',
          {
            rules: [{ required: true, message: 'Please input your username!', whitespace: true }],
          },
        ]"
      />
    </a-form-item>
    <a-form-item v-bind="formItemLayout">
    <span style="color:white; font-size:16px;font-family: 'Helvetica Neue';" slot="label">Phone Number</span>
      <a-input
        v-decorator="[
          'phone',
          {
            rules: [{ required: true, message: 'Please input your phone number!' }],
          },
        ]"
        style="width: 100%"
      >
        <a-select
          slot="addonBefore"
          v-decorator="['prefix', { initialValue: '1' }]"
          style="width: 70px"
        >
          <a-select-option value="1">
            +1
          </a-select-option>
          <a-select-option value="44">
            +44
          </a-select-option>
          <a-select-option value="65">
            +65
          </a-select-option>
        </a-select>
      </a-input>
    </a-form-item>   
    <a-form-item v-bind="tailFormItemLayout">
      <a-checkbox v-decorator="['agreement', { valuePropName: 'checked' }]">
        <span style="color:white; font-size:16px;font-family: 'Helvetica Neue';">I have read the</span>
        <a href="" style="color:white; font-size:16px;font-family: 'Helvetica Neue';">
          agreement
        </a>
      </a-checkbox>
    </a-form-item>
    <a-form-item v-bind="tailFormItemLayout">
      <a-button style="background-color:#ff4d4f; border-color:#ff4d4f" shape="round" size="large" type="primary" html-type="submit">
        Register
      </a-button>
    </a-form-item>
  </a-form>
</template>
<style>
.ant-form-item-label {
    text-align: left;
}
</style>
<script>


export default {
  name: 'antdform',
  data() {
    return {
      confirmDirty: false,
      autoCompleteResult: [],
      formItemLayout: {
        labelCol: {
          xs: { span: 24 },
          sm: { span: 8 },
        },
        wrapperCol: {
          xs: { span: 24 },
          sm: { span: 16 },
        },
      },
      tailFormItemLayout: {
        wrapperCol: {
          xs: {
            span: 24,
            offset: 0,
          },
          sm: {
            span: 16,
            offset: 8,
          },
        },
      },
    };
  },
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: 'register' });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFieldsAndScroll((err, values) => {
        if (!err) {
          console.log('Received values of form: ', values);
        }
      });
    },
    handleConfirmBlur(e) {
      const value = e.target.value;
      this.confirmDirty = this.confirmDirty || !!value;
    },
    compareToFirstPassword(rule, value, callback) {
      const form = this.form;
      if (value && value !== form.getFieldValue('password')) {
        callback('Two passwords that you enter is inconsistent!');
      } else {
        callback();
      }
    },
    validateToNextPassword(rule, value, callback) {
      const form = this.form;
      if (value && this.confirmDirty) {
        form.validateFields(['confirm'], { force: true });
      }
      callback();
    },
    handleWebsiteChange(value) {
      let autoCompleteResult;
      if (!value) {
        autoCompleteResult = [];
      } else {
        autoCompleteResult = ['.com', '.org', '.net'].map(domain => `${value}${domain}`);
      }
      this.autoCompleteResult = autoCompleteResult;
    },
  },
};
</script>
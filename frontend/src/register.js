import Vue from 'vue';
import Antd from 'ant-design-vue';
import reg from './reg';
import 'ant-design-vue/dist/antd.css';
import '../style.css';

Vue.config.productionTip = false;

Vue.use(Antd);

new Vue({
  render: h => h(reg),
}).$mount('#reg');
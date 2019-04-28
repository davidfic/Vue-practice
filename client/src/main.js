import Vue from 'vue'
import App from './App.vue'
import store from './store'; 


// import Framework7 from 'framework7/framework7.esm.bundle.js';
// import Framework7Vue from 'framework7-vue/framework7-vue.esm.bundle.js';
// import 'framework7/css/framework7.bundle.css';
import 'bootstrap/dist/css/bootstrap.css';


import router from './router'


// Framework7.use(Framework7Vue)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

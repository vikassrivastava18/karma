
import { createWebHistory, createRouter } from 'vue-router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import axios from 'axios'

import { createApp } from 'vue'
import App from './App.vue'
import HomePage from './views/HomPage.vue'
import LoginPage from './views/LoginPage.vue'

const routes = [
  { path: '/', component: HomePage},
  { path: '/login', component: LoginPage},
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

let app = createApp(App)
  .use(router)
  .use(store)

app.config.globalProperties.$axios = axios

app.mount('#app')

// Request interceptor
axios.interceptors.request.use((config) => {
  const token = localStorage.getItem('Authentication-Token')
  console.log("Token@: ", token);
  if (token) {
    
    config.headers.Authorization = `Token ${token}`
  }
  return config
})

// // Response interceptor
// axios.interceptors.response.use((response) => {
//   // Handle the response here
//   return response
// }, (error) => {
//   // Handle errors here
//   console.error(error)
//   return Promise.reject(error)
// })
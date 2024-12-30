
import { createWebHistory, createRouter } from 'vue-router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

import { createApp } from 'vue'
import App from './App.vue'
import HomePage from './pages/HomPage.vue'
import LoginPage from './pages/LoginPage.vue'

const routes = [
  { path: '/', component: HomePage},
  { path: '/login', component: LoginPage},
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

createApp(App)
.use(router)
.use(store)
.mount('#app')

// filepath: /c:/Users/vikas/OneDrive/Desktop/karma/frontend/karma/src/main.js


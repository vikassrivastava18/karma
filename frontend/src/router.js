import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './components/HomePage.vue'
import LoginComp from './authentication/LoginComp.vue'


export default createRouter({
history: createWebHistory(),
routes: [
  {
    path: '/',
    component: HomePage,
  },
  {
    path: '/login',
    component: LoginComp,
  },  
]
})
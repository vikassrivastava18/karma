// filepath: /c:/Users/vikas/OneDrive/Desktop/karma/frontend/karma/src/store/index.js
import { createStore } from 'vuex'

const store = createStore({
  state: {
    isAuthenticated: true,
  },
  mutations: {
    login(state) {
      state.isAuthenticated = true
    },
    logout(state) {
      state.isAuthenticated = false
    }
  },
  actions: {
    login({ commit }) {
      commit('login')
    },
    logout({ commit }) {
      commit('logout')
    }
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated
  }
})

export default store
<template>
    <header>
        <div class="p-1">
            <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
                <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                    <h2 style="color: crimson;" class="px-2">KARMA</h2>
                </ul>

                <div class="text-end" v-if="isAuthenticated">
                    <button type="button" class="btn btn-outline-dark me-4" @click="logout">Logout</button>
                </div>
                <div class="text-end" v-else>
                    <button type="button" class="btn btn-outline-dark me-4" @click="login">Login</button>
                    <!-- <button type="button" class="btn btn-warning">Sign-up</button> -->
                </div>
            </div>
        </div>
    </header>
</template>

<script>
import { mapState } from 'vuex'
export default {
    name: 'HeaderComponent',
    computed: {
        ...mapState(['isAuthenticated'])
    },
    methods: {
        logout() {
            localStorage.removeItem('Authentication-Token')
            this.$store.dispatch('logout')
            this.$router.push('/login')
        },
        login() {
            this.$router.push('/login')
        }
    }
}
</script>

<style scoped>
ul {
    float: right;
}
header {
    background-color: #000;
    width: 100vw;
    margin-top: 0px;
}
button {background-color: #fff;}
</style>
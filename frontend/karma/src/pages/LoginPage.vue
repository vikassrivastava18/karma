<template>
    <div class="container">
        <h2>Login</h2>
        <form @submit.prevent="submit">
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Username</label>
                <input type="text" class="form-control" v-model="formData.username" id="exampleInputEmail1"
                    aria-describedby="emailHelp">
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" v-model="formData.password" id="exampleInputPassword1">
            </div>
            <div class="mb-3 form-check">
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Remember Me</label>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>

    </div>

</template>

<script>
/* eslint-disable */
import { mapActions } from 'vuex'

export default {
    name: 'LoginComponent',
    data() {
        return {
            formData: {
                username: null,
                password: null
            }
        }
    },
    methods: {
        ...mapActions(['login']),
        async submit() {
            console.log(this.formData);

            const url = 'http://127.0.0.1:8000/token'
            const init_obj = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.formData)
            }

            try {

                const res = await fetch(url, init_obj)
                if (!res.ok) {
                    const errorData = await res.json()
                    throw new Error(errorData.message || 'Error occurred')
                }
                const data = await res.json()
                console.log('Success:', data)
                // Seth the token in local storage
                localStorage.setItem('Authentication-Token', data.token)
                // Set the state of isAuthenticated to true
                this.login()
                // Redirect to the home page
                this.$router.push({ path: '/' })
                // handle success (e.g., show a success message, redirect, etc.)
            } catch (error) {
                console.error('Error:', error.message)
                // handle error (e.g., show an error message)
            }
        }
    }
}
</script>


<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 30vw;
}

form {
    width: 50%;
    margin: auto;
    padding: 20px;
    background: #dee8ff;
    border-radius: 10px;
}
</style>

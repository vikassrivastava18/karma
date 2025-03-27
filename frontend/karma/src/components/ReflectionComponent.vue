<template>
    <div class="reflection-component card p-4 shadow-sm">
        <h2>Daily Reflection</h2>
        <form @submit.prevent="submitReflection">
            <div class="form-group">
                <textarea id="reflection" v-model="reflection" class="form-control" required></textarea>
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
/* eslint-disable */
const baseUrl = 'http://localhost:8000';
export default {
    name: 'RelectionComponent',
    data() {
        return {
            reflection: ''
        };
    },
    methods: {
        async submitReflection() {
            // Make API call to submit the reflection
            try {
                const url = baseUrl + '/api/reflections'
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Token ' + localStorage.getItem('Authentication-Token')
                    },
                    body: JSON.stringify({ reflection: this.reflection })
                });
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                await response.json();
                this.$emit('showToast')
                this.reflection = '';
            } catch (error) {
                this.$emit('errorToast')
                this.$emit('errorToast')
            }
        }
    }
};
</script>

<style scoped>
.reflection-component {
    max-width: 1150px;
    margin: auto;
    margin-top: 100px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: lightyellow;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

textarea {
    width: 100%;
    height: 100px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>
<template>
    <div class="wrapper">

        <div class="container">
            <h2>
                DAILY
                <!-- Button trigger modal -->
                <button type="button" class="btn px-4" data-bs-toggle="modal" data-bs-target="#exampleModal">
                    <!-- <img src="../assets/create.png" width="20" alt="create list"> -->
                </button>
            </h2>
            <div class="cards-wrapper" :key="todo" @drop="onDrop($event, 'pe')" @dragenter.prevent @dragover.prevent>
                <card v-for="karma of todos" :key="karma.id" :id="karma.id" class="card" draggable="true"
                    @dragstart="startDrag($event, karma.id)">

                    <span class="title">
                        {{ karma.title }}
                    </span>

                    <span class="content" v-html="karma.karma">

                    </span>

                </card>
            </div>
        </div>

        <div class="container" id="satisfied">
            <h2>
                SATISFIED
            </h2>
            <div class="cards-wrapper" :key="satisfied" @drop="onDrop($event, 'sa')" @dragenter.prevent
                @dragover.prevent>
                <card v-for="karma of satisfied" :key="karma.id" :id="karma.id" class="card" draggable="true"
                    @dragstart="startDrag($event, karma.id)">

                    <span class="title">
                        {{ karma.title }}
                    </span>
                    <span class="content" v-html="karma.karma">
                    </span>

                </card>
            </div>
        </div>

        <div class="container" id="unsatisfied">
            <h2>
                UNSATISFIED
            </h2>
            <div class="cards-wrapper" :key="unsatisfied" @drop="onDrop($event, 'us')" @dragenter.prevent
                @dragover.prevent>
                <card v-for="karma of unsatisfied" :key="karma.id" :id="karma.id" class="card" draggable="true"
                    @dragstart="startDrag($event, karma.id)">

                    <span class="title">
                        {{ karma.title }}
                    </span>
                    <span class="content" v-html="karma.karma">
                    </span>

                </card>
            </div>
        </div>

    </div>
</template>

<script>
const baseUrl = 'http://localhost:8000';

export default {
    name: 'DailyComponent',
    data() {
        return {
            karmas: [],
            todos: [],
            satisfied: [],
            unsatisfied: []
        };
    },
    mounted() {
        if (!this.$store.state.isAuthenticated) {
            this.$router.push({ path: '/login' });
        }
        // Get the items from backend
        this.getKarmas()
    },
    methods: {
        async getKarmas() {
            const url = baseUrl + '/api/tasks'
            const init_obj = {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token ' + localStorage.getItem('Authentication-Token')
                },
            }

            try {
                const res = await fetch(url, init_obj)
                if (!res.ok) {
                    const errorData = await res.json()
                    throw new Error(errorData.message || 'Error occurred')
                }
                const data = await res.json()
                this.karmas = data
                this.filterItems()
            } catch (error) {
                console.error('Error:', error.message)
                // handle error (e.g., show an error message)
            }
        },

        async editKarma(id, list) {
            const karma = this.karmas.find(karma => karma.id == id)
            const url = baseUrl + '/api/tasks/' + id
            const init_obj = {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token ' + localStorage.getItem('Authentication-Token')
                },
                body: JSON.stringify({...karma,"review": list})
            }

            try {
                const res = await fetch(url, init_obj)
                if (!res.ok) {
                    const errorData = await res.json()
                    throw new Error(errorData.message || 'Error occurred')
                }
                await res.json()
                this.$emit('showToast')
            } catch (error) {
                console.error('Error:', error.message)
                this.$emit('errorToast')
                // handle error (e.g., show an error message)
            }

        },

        filterItems() {
            this.todos = this.karmas.filter(karma => karma.review === 'pe')
            this.satisfied = this.karmas.filter(karma => karma.review === 'sa')
            this.unsatisfied = this.karmas.filter(karma => karma.review === 'us')

            this.karmas.forEach(karma => {
                karma.src = karma.type
            })
        },

        startDrag(event, id) {
            event.dataTransfer.dropEffect = 'move'
            event.dataTransfer.effectAllowed = 'move'
            event.dataTransfer.setData('itemID', id)
            console.log("card_id", id)
        },

        onDrop(event, list) {
            const itemID = event.dataTransfer.getData('itemID')
            const item = this.karmas.find((karma) => karma.id == itemID)
            item.review = list
            this.filterItems()
            this.editKarma(itemID, list)            
        },        
    }
};
</script>

<style scoped>
.daily-component {
    text-align: center;
    margin: 20px;
}

.type {
        background-color: lightskyblue;
    }

    #satisfied {
        background-color: lightgreen;
    }

    #unsatisfied {
        background-color: lightcoral;
    }
</style>
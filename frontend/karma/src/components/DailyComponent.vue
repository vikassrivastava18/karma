<template>
    <div class="wrapper">
        
        <div class="container fixed-size" id="karma">
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
                        <IconComponent :karmaType="karma.type" />

                    </span>

                    <span class="content" v-html="karma.karma">

                    </span>

                </card>
            </div>
        </div>

        <div class="container fixed-size" id="satisfied">
            <h2>
                SATISFIED
            </h2>
            <div class="cards-wrapper" :key="satisfied" @drop="onDrop($event, 'sa')" @dragenter.prevent
                @dragover.prevent>
                <card v-for="karma of satisfied" :key="karma.id" :id="karma.id" class="card" draggable="true"
                    @dragstart="startDrag($event, karma.id)">

                    <span class="title">
                        {{ karma.title }}
                        <IconComponent :karmaType="karma.type" />
                    </span>
                    <span class="content" v-html="karma.karma">
                    </span>

                </card>
            </div>
        </div>

        <div class="container fixed-size" id="unsatisfied">
            <h2>
                UNSATISFIED
            </h2>
            <div class="cards-wrapper" :key="unsatisfied" @drop="onDrop($event, 'us')" @dragenter.prevent
                @dragover.prevent>
                <card v-for="karma of unsatisfied" :key="karma.id" :id="karma.id" class="card" draggable="true"
                    @dragstart="startDrag($event, karma.id)">

                    <span class="title">
                        {{ karma.title }}
                        <IconComponent :karmaType="karma.type" />
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
import IconComponent from './IconComponent.vue';


export default {
    name: 'DailyComponent',
    components: {
        IconComponent
    },
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
                console.log(data);
                
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

.container {
    background: #dee8ff;
    border-radius: 10px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    max-height: 70vh;
}

.cards-wrapper {
    scrollbar-width: thin;
    padding-inline: 10px;
    padding-top: 10px;
    max-height: calc(100vh - 100px);
    min-width: 328px;
    border-radius: 10px;
    overflow-y: scroll;
    min-height: 100px;
    flex-grow: 1;
    transition: 0.3s;
}

.card-placeable {
    background: #0000000d;
}

.card {
    padding: 10px;
    /* width: 300px; */
    margin-bottom: 10px;
    background: white;
    border-radius: 10px;
    overflow-y: hidden;
    filter: drop-shadow(0 2px 7px #00000040);
    display: flex;
    flex-direction: column;
    cursor: pointer;
}

.type {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding-block: 5px;
    gap: 5px;
    margin: -10px;
    margin-bottom: 10px;
}

.wrapper {
    padding: 30px;
    max-height: 60vh;
    max-width: 80vw;

    /* margin-top: 20vh; */
    display: flex;
    margin: auto;
    justify-content: center;
    align-items: center;
}

.fixed-size {
    margin: 10px;
    margin-top: 50vh;
    padding: 20px;    
    width: 800px; /* Set your desired width */
    height: 600px; /* Set your desired height */
    overflow: auto; /* Add overflow if content exceeds the fixed size */
}
.daily-component {
    text-align: center;
    margin: 20px;
}

#karma {
        background-color: lightyellow;
    }

    #satisfied {
        background-color: lightgreen;
    }

    #unsatisfied {
        background-color: #e99292;
    }
</style>
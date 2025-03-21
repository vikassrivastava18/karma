<template>
    <div class="wrapper2">

        <div class="container fixed-size" id="todo">
            <h2>
                TODO
                <!-- Button trigger modal -->
                <button type="button" class="btn px-4" data-bs-toggle="modal" data-bs-target="#exampleModal">
                    <img src="../assets/create.png" width="20" alt="create list" id="addItemBtn">
                </button>
            </h2>
            <div class="cards-wrapper" :key="todo" @drop="onDrop($event, 'to')" @dragenter.prevent @dragover.prevent>
                <card v-for="karma of todos" :key="karma.id" :id="karma.id" class="card" draggable="true"
                    @dragstart="startDrag($event, karma.id)">
                    <span class="">
                        {{ karma.todo }}
                        <IconComponent :karmaType="karma.todo_type" />
                    </span>
                </card>
            </div>
        </div>

        <div class="container fixed-size" id="inProgress">
            <h2>
                IN-PROGRESS
            </h2>
            <div class="cards-wrapper" :key="inProgress" @drop="onDrop($event, 'pr')" @dragenter.prevent
                @dragover.prevent>
                <card v-for="karma of inProgress" :key="karma.id" :id="karma.id" class="card" draggable="true"
                    @dragstart="startDrag($event, karma.id)">
                    <span class="">
                        {{ karma.todo }}
                        <IconComponent :karmaType="karma.todo_type" />
                    </span>
                </card>
            </div>
        </div>

        <div class="container fixed-size" id="complete">
            <h2>
                COMPLETED
            </h2>
            <div class="cards-wrapper" :key="complete" @drop="onDrop($event, 'co')" @dragenter.prevent
                @dragover.prevent>
                <card v-for="karma of complete" :key="karma.id" :id="karma.id" class="card" draggable="true"
                    @dragstart="startDrag($event, karma.id)">

                    <span class="">
                        {{ karma.todo }} {{ karma.todo_type }}
                        <IconComponent :karmaType="karma.todo_type" />
                    </span>

                </card>
            </div>
        </div>

    </div>

    <ModalComponent @refreshTodoData="getTodos" @showToast="this.$emit('showToast')" />
</template>

<script>
/* eslint-disable */
import IconComponent from './IconComponent.vue';
import ModalComponent from './ModalComponent.vue';

const baseUrl = 'http://localhost:8000';
let data = [
    {
        "id": 1,
        "todo": "Finish first CS50 assignment",
        "todo_type": "st",
        "status": "co",
        "created_on": "2025-01-25",
        "deadline": "2025-01-10"
    },
    {
        "id": 2,
        "todo": "Do some DSA",
        "todo_type": "st",
        "status": "pr",
        "created_on": "2025-02-03",
        "deadline": "2025-01-29"
    },
    {
        "id": 3,
        "todo": "Do some DSA",
        "todo_type": "st",
        "status": "pr",
        "created_on": "2025-01-25",
        "deadline": "2025-01-30"
    },
    {
        "id": 4,
        "todo": "Learn some Python skills",
        "todo_type": "st",
        "status": "co",
        "created_on": "2025-01-26",
        "deadline": "2025-01-27"
    },
    {
        "id": 5,
        "todo": "Do something",
        "todo_type": "st",
        "status": "to",
        "created_on": "2025-01-25",
        "deadline": "2025-01-29"
    },
    {
        "id": 6,
        "todo": "Play 20 matches by 31",
        "todo_type": "pl",
        "status": "co",
        "created_on": "2025-02-03",
        "deadline": "2025-01-31"
    }
]

export default {
    name: 'TodoComponent',
    components: {
        IconComponent,
        ModalComponent
    },
    data() {
        return {
            AllTasks: [],
            todos: [],
            inProgress: [],
            complete: []
        };
    },
    mounted() {
        // Get the items from backend
        this.AllTasks = data
        this.filterItems()
        // this.getTodos()
    },
    methods: {
        async getTodos() {
            const url = baseUrl + '/api/todos'
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
                this.AllTasks = data

                this.filterItems()
            } catch (error) {
                console.error('Error:', error.message)
                // handle error (e.g., show an error message)
            }
        },

        async editKarma(id, list) {
            this.$emit('showToast')
            return
            // Modify for API
            const karma = this.AllTasks.find(karma => karma.id == id)
            const url = baseUrl + '/api/todos/' + id
            const init_obj = {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token ' + localStorage.getItem('Authentication-Token')
                },
                body: JSON.stringify({ ...karma, "review": list })
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
            }

        },

        filterItems() {
            this.todos = this.AllTasks.filter(karma => karma.status === 'to')
            this.inProgress = this.AllTasks.filter(karma => karma.status === 'pr')
            this.complete = this.AllTasks.filter(karma => karma.status === 'co')

            this.AllTasks.forEach(todo => {
                todo.src = todo.type
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
            const item = this.AllTasks.find(karma => karma.id == itemID)
            item.status = list
            this.filterItems()
            this.editKarma(itemID, list)
        },
    }
};
</script>

<style scoped>
.wrapper2 {
    padding: 30px;
    max-height: 60vh;
    max-width: 80vw;

    /* margin-top: 20vh; */
    display: flex;
    margin: auto;
    margin-top: 45vh;
    justify-content: center;
    align-items: center;
}

.container {
    background: #dee8ff;
    border-radius: 10px;
    padding: 20px;
    margin: 10px;
    display: flex;
    flex-direction: column;
    max-height: 70vh;
}

.cards-wrapper {
    scrollbar-width: thin;
    padding-inline: 10px;
    padding-top: 10px;
    /* max-height: calc(100vh - 100px); */
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
    margin-bottom: 20px;
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


.fixed-size {
    /* margin-top: 80vh; */
    padding: 20px;
    width: 800px;
    /* Set your desired width */
    height: 500px;
    /* Set your desired height */
    overflow: auto;
    /* Add overflow if content exceeds the fixed size */
}

.daily-component {
    text-align: center;
    margin: 20px;
}

#todo {
    background-color: lightyellow;
}

#inProgress {
    background-color: lightblue;
}

#complete {
    background-color: lightgreen;
}
</style>
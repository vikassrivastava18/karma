<template>
    <div class="wrapper2">

        <div class="container fixed-size" id="todo">
            <h2>
                TODO
                <!-- Button trigger modal -->
                <button type="button" class="btn px-2" data-bs-toggle="modal" data-bs-target="#exampleModal">
                    <img src="../assets/create.png" width="20" alt="create list">
                </button>
            </h2>
            <div class="cards-wrapper" :key="todo" @drop="onDrop($event, 'to')" @dragenter.prevent @dragover.prevent>
                <card v-for="karma of todos" :key="karma.id" :id="karma.id" class="card" draggable="true"
                    @dragstart="startDrag($event, karma.id)" @dblclick="openDetails(karma)">
                    <span>
                    <h5>{{ karma.todo }}
                        <IconComponent :type="karma.todo_type" />
                    </h5>
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
                    @dragstart="startDrag($event, karma.id)" @dblclick="openDetails(karma)">
                    <span>
                        <h5> {{ karma.todo }}
                            <IconComponent :type="karma.todo_type" />
                        </h5>
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
                    @dragstart="startDrag($event, karma.id)" @dblclick="openDetails(karma)">

                    <span>
                        <h5>{{ karma.todo }}
                            <IconComponent :type="karma.todo_type" />
                        </h5>
                    </span>

                </card>
            </div>
        </div>

    </div>

    <ModalComponent @getTodos="getTodos" />

    <div v-if="showDetails" class="details-modal">
        <div class="details-content">
            <h3>Todo Details</h3>
            <p><strong>Title:</strong> {{ selectedTodo.todo }}</p>
            <p><strong>Status:</strong> {{ selectedTodo.status }}</p>
            <p><strong>Type:</strong> {{ selectedTodo.todo_type }}</p>
            <button @click="closeDetails">Close</button>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import IconComponent from './IconComponent.vue';
import ModalComponent from './ModalComponent.vue';

const baseUrl = 'http://localhost:8000';

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
            complete: [],
            showDetails: false,
            selectedTodo: null
        };
    },

    mounted() {
        // Get the items from backend
        this.getTodos()
    },
    methods: {
        truncate(text, length) {
            if (!text) return '';
            return text.length > length ? text.substring(0, length) + '...' : text;
        },
        async getTodos() {
            const url = baseUrl + '/api/todos'

            try {
                const res = await this.$axios.get(url)
                const data = res.data
                this.AllTasks = data
                this.filterItems()
            } catch (error) {
                console.error('Error:', error.message)
                // handle error (e.g., show an error message)
            }
        },

        filterItems() {
            this.todos = this.AllTasks.filter(karma => karma.status === 'to')
            this.inProgress = this.AllTasks.filter(karma => karma.status === 'pr')
            this.complete = this.AllTasks.filter(karma => karma.status === 'co')
            console.log("todos", this.todos);
            console.log("inProgress", this.inProgress);
            console.log("complete", this.complete);

            this.AllTasks.forEach(todo => {
                todo.src = todo.type
            })
        },
        openDetails(todo) {
            this.selectedTodo = todo;
            this.showDetails = true;
        },

        closeDetails() {
            this.selectedTodo = null;
            this.showDetails = false;
        },

        async editKarma(id, list) {
            // Modify for API
            const karma = this.AllTasks.find(karma => karma.id == id)
            const url = baseUrl + '/api/todos/' + id
            const updatedData = { ...karma, "review": list }

            try {
                await this.$axios.put(url, updatedData)
                this.$emit('showToast')
            } catch (error) {
                console.error('Error:', error.message)
                this.$emit('errorToast')
            }

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
    padding-top: 45px;
    /* max-height: 60vh; */
    max-width: 80vw;
    display: flex;
    margin: auto;
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

.details-modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.details-content {
    background: #fff;
    padding: 30px;
    border-radius: 10px;
    min-width: 300px;
    box-shadow: 0 2px 10px #0003;
}
</style>
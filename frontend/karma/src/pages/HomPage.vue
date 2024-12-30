<template>
    <div class="wrapper">
        
        <div class="container"            
            >
            <h2>
                TODO             
                <!-- Button trigger modal -->
                <button type="button" class="btn px-4" data-bs-toggle="modal" data-bs-target="#exampleModal">
                    <img src="../assets/create.png" width="20" alt="create list">
                </button>            
            </h2>
            <div class="cards-wrapper"
                :key="todo"
                @drop="onDrop($event, 'todo')"
                @dragenter.prevent
                @dragover.prevent>
                <card v-for="karma of todos" 
                    :key="karma.id" :id="karma.id" class="card"
                    draggable="true"
                    @dragstart="startDrag($event, karma.id)">
                    <div class="type">
                        <span class="type-text">
                            {{ karma.type }}
                        </span>
                    </div>
                    <span class="title">
                        {{ karma.title }}
                    </span>
                    <span class="content">
                        {{ karma.content }}
                    </span>

                </card>
            </div>
        </div>

        <div class="container" id="satisfied"
            >
            <h2>
                SATISFIED
            </h2>
            <div class="cards-wrapper"
                :key="satisfied"
                @drop="onDrop($event, 'satisfied')"
                @dragenter.prevent
                @dragover.prevent>
                <card v-for="karma of satisfied" 
                    :key="karma.id" :id="karma.id" class="card"
                    draggable="true"
                    @dragstart="startDrag($event, karma.id)">
                    <div class="type">
                        <span class="type-text">
                            {{ karma.type }}
                        </span>
                    </div>
                    <span class="title">
                        {{ karma.title }}
                    </span>
                    <span class="content">
                        {{ karma.content }}
                    </span>

                </card>
            </div>
        </div>

        <div class="container" id="unsatisfied"
            >
            <h2>
                UNSATISFIED
            </h2>
            <div class="cards-wrapper"
                :key="unsatisfied"
                @drop="onDrop($event, 'unsatisfied')"
                @dragenter.prevent
                @dragover.prevent>
                <card v-for="karma of unsatisfied" 
                    :key="karma.id" :id="karma.id" class="card"
                    draggable="true"
                    @dragstart="startDrag($event, karma.id)">
                    <div class="type">
                        <span class="type-text">
                            {{ karma.type }}
                        </span>
                    </div>
                    <span class="title">
                        {{ karma.title }}
                    </span>
                    <span class="content">
                        {{ karma.content }}
                    </span>

                </card>
            </div>
        </div>

    </div>

    <ToastComponent />

    <ModalComponent />
</template>


<script>
/* eslint-disable */
// import CustomFetch from '@/CustomFetch';
import { mapState } from 'vuex'
import { Toast } from 'bootstrap'
import ModalComponent from '../components/ModalComponent.vue';
import ToastComponent from '../components/ToastComponent.vue';

export default {
    name: 'HomePage',
    computed: {
        ...mapState(['isAuthenticated']),
    },
    components: {
        ModalComponent,
        ToastComponent
    },
    data() {
        return {
            karmas: [
                {
                id: 1,
                title: 'Test Story',
                content: 'This is test content of a story. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam',
                priority: 'low',
                type: 'pray',
                status: 'todo',
                src: '..assets/pray.svg'
            },
            {
                id: 2,
                title: 'Code Push',
                content: 'This is test content of a story. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam',
                priority: 'low',
                type: 'study',
                status: 'todo',
                src: '..assets/pray.svg'
            },
            {

                id: 3,
                title: 'Test Story',
                content: 'This is test content of a story. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam',
                priority: 'low',
                type: 'prayer',
                status: 'satisfied',
                src: '..assets/pray.svg'
            },
            {
                id: 4,
                title: 'Code Push',
                content: 'This is test content of a story. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam',
                priority: 'low',
                type: 'work',
                status: 'satisfied',
                src: '..assets/pray.svg'
            },
            {

                id: 5,
                title: 'Test Story',
                content: 'This is test content of a story. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam',
                priority: 'low',
                type: 'pray',
                status: 'unsatisfied',
                src: '..assets/pray.svg'
            },
            {
                id: 6,
                title: 'Code Push',
                content: 'This is test content of a story. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam',
                priority: 'low',
                type: 'work',
                status: 'unsatisfied',
                src: '..assets/pray.svg'
            }
        ],
        todos: [],
        satisfied: [],
        unsatisfied: []            
        }
    },
    mounted() {
        // Check if the user is authenticated
        console.log("Authenticated?", this.$store.state.isAuthenticated);
        
        if (!this.$store.state.isAuthenticated) {
            this.$router.push({path: '/login'});
        }

        this.filterItems()
        // self = this
        // CustomFetch(`http://127.0.0.1:8080/api/token-test`, {
        //     method: 'GET',

        //     headers: {
        //         'Content-Type': 'application/json',
        //         'Authorization': localStorage.getItem(
        //             'Authentication-Token'
        //         ),
        //     },
        // })
        //     .then((data) => {
        //         if (data.status == 'fail') {
        //             // self.$router.push({ path: '/login' });
        //         }
        //         else {
        //             this.lists_data = data.slice(1)
        //             this.lists = data[0]['lists']
        //             console.log(this.lists)
        //         }

        //     })
        //     .catch((err) => {
        //         //   alert(err.message)
        //         console.log(err.message, err.status)

        //     })
    },
    
    methods: {
        showToast() {
            const toastEl = document.getElementById('liveToast')
            const toast = new Toast(toastEl)
            toast.show()
        },
        getImgUrl(pet) {
            var images = require.context('../assets/', false, /\.png$/)
            return images('../assets/' + pet + ".svg")
        },
        filterItems () {
            this.todos = this.karmas.filter(karma => karma.status === 'todo')
            this.satisfied = this.karmas.filter(karma => karma.status === 'satisfied')
            this.unsatisfied = this.karmas.filter(karma => karma.status === 'unsatisfied')

            this.karmas.forEach(karma => {
                karma.src = karma.type
            })

        },
        startDrag (event, id){
            event.dataTransfer.dropEffect = 'move'
            event.dataTransfer.effectAllowed = 'move'
            event.dataTransfer.setData('itemID', id)
            console.log("card_id",id)            
        },

        onDrop(event, list) {
            const itemID = event.dataTransfer.getData('itemID')
            const item = this.karmas.find((karma) => karma.id == itemID)            
            item.status = list
            this.filterItems()
            this.showToast()
            // event.target.appendChild(document.getElementById(itemID));                        
        },
        
    }
}

</script>

<style scoped>
    .type {
        background-color: lightskyblue;
    }
    #satisfied {
        background-color: lightgreen;
    }
    #unsatisfied {
        background-color: lightcoral;
    }
    .btn {
        float: right;
    }
</style>


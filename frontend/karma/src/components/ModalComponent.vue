<template>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Add Task</h5>
                    <button type="button" class="btn-close" 
                    id="closeModal" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="createTask">
                        <div class="mb-3">
                            <label for="taskName" class="form-label">Task Name</label>
                            <input type="text" class="form-control" 
                                   v-model="task.todo" id="taskName"
                                aria-describedby="emailHelp">
                        </div>
                        <div class="mb-3">
                            <label for="taskType" class="form-label">Task Type</label>
                            <select name="taskType" id="taskType" 
                                v-model="task.todo_type" class="form-select">
                                <option value="pr">PRAYER</option>
                                <option value="st">STUDY</option>
                                <option value="wo">WORK</option>
                                <option value="ho">FAMILY</option>
                                <option value="pu">PUBLIC</option>
                                <option value="pl">PLAY</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label class="form-label" for="setTimeline">Set Timeline</label>
                            <input type="date" 
                            v-model="task.deadline" class="form-control" id="setTimeline">                            
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
const baseUrl = 'http://localhost:8000';

export default {
    data() {
        return {
            task: {
                todo: '',
                todo_type: 'pl',
                deadline: ''
            }
        };
    },
    methods: {
        async createTask () {
            console.log(this.task);
            // Make API for submission
            const url = baseUrl + '/api/todos'
            const init_obj = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token ' + localStorage.getItem('Authentication-Token')
                },
                body: JSON.stringify(this.task)
            }

            try {
                const res = await fetch(url, init_obj)
                if (!res.ok) {
                    const errorData = await res.json()
                    throw new Error(errorData.message || 'Error occurred')
                }
                await res.json()                
                this.$emit('refreshTodoData')
                // Close the modal
                const modalCloseBtn = document.getElementById('closeModal')
                modalCloseBtn.click()
                // Reset the form
                this.task = {
                    todo: '',
                    todo_type: '',
                    deadline: ''
                };
                this.$emit('showToast')

            } catch (error) {
                console.error('Error:', error.message)
                // handle error (e.g., show an error message)
            }
            

        }
    },

}

</script>
<template>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Add Task</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @submit="createTask">
                        <div class="mb-3">
                            <label for="taskName" class="form-label">Task Name</label>
                            <input type="text" class="form-control" id="taskName"
                                aria-describedby="emailHelp">
                        </div>
                        <div class="mb-3">
                            <label for="taskType" class="form-label">Task Type</label>
                            <select name="taskType" id="taskType" class="form-select">
                                <option value="1">PRAYER</option>
                                <option value="2">STUDY</option>
                                <option value="3">WORK</option>
                                <option value="4">FAMILY</option>
                                <option value="5">PUBLIC</option>
                                <option value="6">PLAY</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label class="form-label" for="setTimeline">Set Timeline</label>
                            <input type="date" class="form-control" id="setTimeline">                            
                        </div>
                        <button type="submit" class="btn btn-primary">Submit</button>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    methods: {
        createTask (e) {
            e.preventDefault()
            // Make API for submission
        }
    }
}

</script>
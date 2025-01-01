<template>
    <!-- Toast -->
    <div class="position-fixed top-0 end-0 p-3" style="z-index: 11">
    <div id="liveToastError" class="toast hide" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
            <strong class="me-auto">Update Failed</strong>
            <small>Just Now</small>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            Some error occured!
        </div>
    </div>
</div>
</template>

<script>
</script>

<style scoped>
.toast-header {
    background-color: #e03d4b;
    color: #fcf2f3;
    border-bottom: 1px solid #f5c6cb;
}
</style>
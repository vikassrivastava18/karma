<template>
        <!-- Toast -->
        <div class="position-fixed bottom-0 start-0 p-3" style="z-index: 11">
        <div id="liveToast" class="toast hide" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="toast-header">
                <strong class="me-auto">Update</strong>
                <small>Just Now</small>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
                Items's status has been updated
            </div>
        </div>
    </div>
</template>

<script>
</script>

<style>
.toast-header {
    background-color: #d1ecf1;
    color: #0c5460;
    border-bottom: 1px solid #bee5eb;
}
</style>
<template>

    <img v-if="karmaType === 'pr'" src="../assets/pray.svg" alt="" width="25">
    <img v-if="karmaType === 'wo'" src="../assets/work-2.svg" alt="" width="25">
    <img v-if="karmaType === 'pl'" src="https://www.svgrepo.com/show/465153/game-console-cable.svg" alt="" width="25">
    <img v-if="karmaType === 'st'" src="../assets/study-2.svg" alt="" width="25">
    <img v-if="karmaType === 'pu'" src="../assets/public.svg" alt="" width="25">
    <img v-if="karmaType === 'ho'" src="https://www.svgrepo.com/show/483728/family.svg" alt="" width="25">

</template>

<script>

export default {
    name: 'IconComponent',
    props: {
        karmaType: {
            type: String,
            required: true
        }
    },
    computed: {

    }
}
</script>

<style scoped>
img {
    position: absolute;
    right: 10px;
}
</style>
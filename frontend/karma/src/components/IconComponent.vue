<template>

    <img v-if="karmaType === 'pr'" src="../assets/pray.svg" alt="" width="20">
    <img v-if="karmaType === 'wo'" src="../assets/work.svg" alt="" width="20">
    <!-- <img v-if="karmaType === 'pr'" src="../assets/pray.svg" alt="" width="20"> -->

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
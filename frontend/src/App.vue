<template>
    <header class="p-2 mb-2">
        <h2>Digi-Diary</h2>
    </header>

    <nav class="p-2" style="color: #fff;">

    </nav>

    <main>
        <div class="container mt-4 p-4">
            <router-view></router-view>
        </div>
        
    </main>
</template>

<script>

export default {
    components: {
    }
}
</script>

<style>
body {
    background-color: #fff;
    background-image:
    /* linear-gradient(90deg, transparent 79px, #abced4 79px, #abced4 81px, transparent 81px), */
    linear-gradient(#eee .1em, transparent .1em);
    background-size: 100% 1.2em;
}

header>h2 {
    color: crimson;
    background-color: lightgrey;
    padding: 8px;
}

.karma,
.doing,
.done {
    padding: 10px;
    border: 2px solid white;
}

.karma {
    background-color: lightcoral;
}

.doing {
    background-color: lightgoldenrodyellow;
}

.done {
    background-color: lightgreen;
}

h4 {
    color: #3a0a0a;
}
</style>

<template>
    <div>
        <h3>Chores</h3>
        <div class="chores">
        <!-- <h3>Add Chore</h3> -->


            <div v-for="chore in allChores" :key="chore.id" class="chore">
                {{ chore.title }}
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    name: "Chores",
    methods: {
        ...mapActions(['fetchChores']),
    },
    computed: mapGetters(['allChores']),
    created() {
        this.fetchChores();
    }
}
</script>

<style >
    .chores {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-gap: 1rem;
    }
    .chore {
        border: 1px solid #ccc;
        background: #41b883;
        padding: 1rem;
        border-radius: 5px;
        text-align: center;
        position: relative;
        cursor: pointer;
    }
</style>

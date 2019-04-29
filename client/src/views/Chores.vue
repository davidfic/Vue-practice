<template>
    <div class="container">
        <AddChore />
        <Chores />
    </div>
</template>

<script>
import Chores from "../components/Chores"
import AddChore from '../components/AddChore'

export default {
    components: {
        Chores,
        AddChore,
    }
}
</script>

<style>

</style>

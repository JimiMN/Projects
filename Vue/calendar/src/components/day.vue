<template>
    <div id="dayDiv">
        <span>{{ dayNumber }}</span>
    </div>
</template>
  
<script>
export default {
    name: 'Day',
    props: {
        givenDay: {
            type: Number,
            default: 1
        }
    },
    data() {
        return {
            dayNumber: this.givenDay
        };
    },
}
</script>
  
<style scoped>

#dayDiv {
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px;
    border-style: solid;
    padding: 10px;
}

</style>
  
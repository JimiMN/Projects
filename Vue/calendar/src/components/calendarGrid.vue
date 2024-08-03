<template>
    <div id="box">
      <ul v-for="n in 31" :key="n">
        <day :givenDay="n"/>
      </ul>
    </div>
</template>
  
<script setup>
    import day from './day.vue';
</script>
  
<style scoped>

#box {
  display: grid;
  grid-template-columns: repeat(7, 1fr); /* 7 columns for the days of the week */
  gap: 5px;
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  background-color: cyan;
}
</style>
  
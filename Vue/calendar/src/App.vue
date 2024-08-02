<script setup>
  import myCalendar from './components/calendar.vue'
</script>

<template>
  <div id="container">
    <div id="calendarDiv">
      <myCalendar/>
    </div>
  </div>
</template>

<style>
/* Remove default margin and padding */
* {
  margin: 0;
  padding: 0;
}

#container {
    display: flex;
    height: 100vh;
    width: 100vw;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}
</style>

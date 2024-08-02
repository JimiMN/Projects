<template>
    <div>
        <div id="box">
            <button id="previous">
                <
            </button>
            <p id="month">
                Kuukausi
            </p>
            <button id="nexy">
                >
            </button>
        </div>
    </div>
</template>
  
<script setup>
  // Add any logic for the header if needed
</script>
  
<style scoped>

#box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: grey;
  border: 1px solid #ccc;
  width: 300px;
  height: 50px;
  padding: 0 20px;
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
}

#previous {
    justify-content: flex-start;
}

#month{
    justify-content: center;
    align-items: center;
}

#next{
    justify-content: flex-end;
    right: 0;
}

</style>
  
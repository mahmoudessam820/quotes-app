<template>
  <div id="home">
    
    <Quotes />

  </div>

</template>

<script>
// @ is an alias to /src
import Quotes from "@/components/quotes/Quotes.vue";

export default {
  name: "Home",
  components: {
    Quotes,
  },
};
</script>

<style scoped>

</style>
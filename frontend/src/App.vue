<template>
  <div id="app">
    <NavBar />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import NavBar from "./components/navbar/NavBar.vue";
import Footer from "./components/footer/Footer.vue";

export default {
  name: "app",
  components: {
    NavBar,
    Footer,
    
  }, 
}

</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #F0F0F0
  /* background: radial-gradient(farthest-side ellipse at 10% 0,#333867,#17193b); */
}
</style>

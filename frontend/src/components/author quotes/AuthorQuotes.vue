<template>
  <div class="author-quotes">
    <div class="container">
      <h1 class="text-center">{{ author }}</h1>
      <img :src="image" :alt="author" class="img-thumbnail mx-auto d-block" />
      <ul v-for="(quote, quote_idx) in quotes" :key="quote_idx" class="m-3">
        <li>{{ quote }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "authorQuotes",
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  async created() {
    const path = "http://127.0.0.1:5000/";
    const response = await fetch(path);
    const data = await response.json();
    this.author = data.authors[this.id];
    this.image = data.images[this.author];
    this.quotes = data.quotes[this.author];
  },
  data() {
    return {
      author: '',
      image: '',
      quotes: [],
    };
  },

};
</script>

<style scoped>
li {
  font-weight: 600;
}
</style>
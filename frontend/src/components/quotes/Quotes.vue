<template>
  <section id="main-quotes" class="m-3">
    <div class="container">
      <h1 class="text-center">Quotes</h1>
      <div class="row">
        <div class="col-sm-12 col-md-6 col-lg-3 py-3" v-for="(author, index) in authors" :key="index">
          <div class="card">
            <img :src="images[author]" :alt="author" />
            <h5 class="card-title text-center fw-bold">{{ author }}</h5>
            <router-link :to="{name:'author', params:{id:index}}" class="btn btn-info">
              Quotes
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Quotes',
  async created() {
    const path = "http://127.0.0.1:5000/";
    const response = await fetch(path);
    const data = await response.json();
    this.authors = data.authors;
    this.images = data.images;
    this.quotes = data.quotes;
  },
  data() {
    return {
      authors: [],
      images: {},
      quotes: {},
    };
  }
};
</script>

<style>
.card {
  width: 251px;
  border-radius: 10px;
}

.card img {
  width: 251px;
  height: 322px;
  object-fit: cover;
  border-radius: 10px;
}
</style>
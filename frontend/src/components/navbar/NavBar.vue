<template>
  <div class="bg">
    <div class="container">
      <nav id="nav" class="navbar navbar-expand-lg text-white ">
        <router-link to="/" class="navbar-brand" >Quotes</router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item ">
              <router-link to="/" class="nav-link">Home <span class="sr-only">(current)</span></router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">About</a>
            </li>

          </ul>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBar"
}
</script>

<style scoped> 
.bg {
  background-color: #142433;
}

</style>
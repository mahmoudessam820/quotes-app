import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import AuthorQuotes from "../components/author quotes/AuthorQuotes.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/author/:id",
    name: "author",
    component: AuthorQuotes,
    props: true,
  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

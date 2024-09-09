<!-- <template>
  
  <Hero />

  <div class="mx-auto grid grid-cols-3 gap-4">
  <div
    class="p-4 bg-white border border-gray-200 rounded-lg"
    v-for="post in posts"
    v-bind:key="post.id"
  >
    <FeedItem v-bind:post="post" v-on:deletePost="deletePost" />
  </div>
</div>

  

 
</template>

<script>
import axios from "axios";

import FeedItem from "../components/FeedItem.vue";
import Hero from "../components/Hero.vue";

export default {
  name: "FeedView",

  components: {
    FeedItem,
    Hero,
    
    
   
 
   
  },

  data() {
    return {
      posts: [],
      body: "",
    };
  },

  mounted() {
    this.getFeed();
  },

  methods: {
    getFeed() {
      axios
        .get("/api/posts/")
        .then((response) => {
          console.log("data", response.data);

          this.posts = response.data;
        })
        .catch((error) => {
          console.log("error", error);
        });
    },

    deletePost(id) {
      this.posts = this.posts.filter((post) => post.id !== id);
    },
  },
};
</script> -->


<template>
  <!-- HERO -->
  <Hero />

  <FilterComponent 
    :categories="categories" 
    :breeds="breeds" 
    @filter-ads="filterAds"
  />

  <div class="mx-auto grid grid-cols-3 bg-orange-50 gap-4">
    <div
      class="p-4 bg-yellow-50 border border-gray-200 rounded-lg"
      v-for="post in filteredPosts"
      :key="post.id"
    >
      <FeedItem :post="post" @deletePost="deletePost" />
    </div>
  </div>
  <Adoption/>

</template>

<script>
import axios from "axios";
import FeedItem from "../components/FeedItem.vue";
import Hero from "../components/Hero.vue";
import FilterComponent from "../components/FilterComponent.vue";
import Adoption from "../components/Adoption.vue";


export default {
  name: "FeedView",
  components: {
    FeedItem,
    Hero,
    FilterComponent,
    Adoption
  
  },
  data() {
    return {
      posts: [],
      filteredPosts: [],
      categories: ["Dog", "Cat", "Bird", "Other"],
      breeds: ["German", "Breed2", "Breed3", "Other"],
    };
  },
  mounted() {
    this.getFeed();
  },
  methods: {
    getFeed() {
      axios
        .get("/api/posts/")
        .then((response) => {
          this.posts = response.data;
          this.filteredPosts = this.posts; // Initially, all posts are displayed
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
    deletePost(id) {
      this.filteredPosts = this.filteredPosts.filter((post) => post.id !== id);
    },
    filterAds(filters) {
      this.filteredPosts = this.posts.filter(post => {
        return (
          (filters.category ? post.category === filters.category : true) &&
          (filters.breed ? post.breed === filters.breed : true) &&
          (filters.minPrice ? post.price >= filters.minPrice : true) &&
          (filters.maxPrice ? post.price <= filters.maxPrice : true)
        );
      });
    },
  },
};
</script>

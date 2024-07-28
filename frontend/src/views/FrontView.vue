<!-- src/App.vue -->
<template>
    <div>
      <Hero />
      <PetList />
      <Adoption />
      <Events />
      <Footer />
    </div>
  </template>
  
  <script>
  import Hero from '../components/Hero.vue'
  import PetList from '../components/PetList.vue'
  import Events from '../components/Events.vue'
  import Adoption from '../components/Adoption.vue'
  import Footer from '../components/Footer.vue'
  
  export default {
    name: 'FrontView',
    components: {
      Hero,
      PetList,
      Events,
      Adoption,
      Footer,
    }
  }
  </script>
  
  <style>
  @import 'tailwindcss/tailwind.css';
  
  
  </style>

<!-- src/components/Hero.vue -->
<template>
    <div>
      <Header />
      <section class="relative bg-[url('/HeroBanner.png')] p-8 text-center bg-cover bg-center h-screen">
        <div class="absolute inset-0 bg-opacity-50 flex flex-col items-start justify-center text-white p-12 z-0">
          <h1 class="text-blue-900 text-5xl font-bold">One More Friend</h1>
          <p class="text-blue-900 text-3xl mt-2">Thousands More Fun!</p>
          <p class="text-blue-900 mt-6 max-w-xl">Having a pet means you have more joy, a new friend, a happy person who will always be with you to have fun. We have 200+ different pets that can meet your needs!</p>
          <div class="mt-6">
            <button class="bg-blue-900 text-white px-6 py-2 rounded mr-2">View Intro</button>
            <button class="bg-blue-900 text-white px-6 py-2 rounded">Explore Now</button>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import Header from './Header.vue'
  
  export default {
    name: 'Hero',
    components: {
      Header,
    }
  }
  </script>
  
  <style scoped>
  </style>
  
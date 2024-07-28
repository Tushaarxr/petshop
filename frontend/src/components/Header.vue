<!-- src/components/Header.vue -->
<template>
    <header class="px-8 py-4 flex justify-between items-center bg-orange-100 z-10">
      <div class="text-3xl text-blue-900 font-bold">Petify</div>
      <nav>
        <ul class="flex space-x-4">
          <li><router-link to="/" class="hover:text-blue-900">Home</router-link></li>
          <li><router-link to="/about" class="hover:text-blue-900">About</router-link></li>
          <li><router-link to="/contact" class="hover:text-blue-900">Contact</router-link></li>
        </ul>
      </nav>
      <div>
        <router-link to="/login">
          <button class="border-2 bg-blue-900 text-white px-6 py-2 rounded-3xl mr-2">Login</button>
        </router-link>
        <router-link to="/signup">
          <button class="bg-blue-900 text-white px-6 py-2 rounded-3xl">Sign Up</button>
        </router-link>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: 'Header',
  }
  </script>
  
  <style scoped>
  </style>
  
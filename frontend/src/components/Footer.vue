<!-- src/components/Footer.vue -->
<template>
    <footer class="bg-orange-100 p-8  text-center">
        <div class="flex justify-center">
      <h2 class="text-2xl ml-12 text-blue-900 font-sans font-semibold">Register Now So You Don't Miss Our Programs</h2>
      <div class="ml-6">
        <input type="email" placeholder="Enter your Email" class="px-4 py-2 rounded mr-2">
        <button class="bg-blue-900 text-white px-4 py-2 rounded">Subscribe Now</button>
      </div></div>
      <div class="mt-6">
        <a href="#" class="mr-4">Home</a>
        <a href="#" class="mr-4">Category</a>
        <a href="#" class="mr-4">About</a>
        <a href="#">Contact</a>
      </div>
      <p class="mt-4">© 2024 Petify. All rights reserved.</p>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'Footer',
  }
  </script>
  
  <style scoped>
  </style>
  
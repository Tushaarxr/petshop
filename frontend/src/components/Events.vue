<!-- src/components/Events.vue -->
<template>
    <section class="bg-yellow-50 p-8">
        <div class="flex justify-between">
      <h2 class="text-2xl ml-12 text-blue-900 font-sans font-semibold text-center">Events Near By You</h2>
      <button class="p-2 px-3 border-2 border-blue-900 font-semibold text-lg mr-20 rounded-xl text-blue-900">Explore More</button>
    </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 mt-6">
        <div v-for="event in events" :key="event.id" class="bg-white p-4 shadow rounded-lg">
          <img :src="event.image" alt="event" class="w-full h-40 object-cover rounded">
          <h3 class="mt-2 text-xl font-bold">{{ event.name }}</h3>
          <p class="text-gray-600">{{ event.description }}</p>
          <p class="text-gray-600">Date: {{ event.date }}</p>
          <p class="text-gray-600">Location: {{ event.location }}</p>
          <button class="bg-blue-900 text-white px-4 py-2 rounded mt-2">Register</button>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    name: 'Events',
    data() {
      return {
        events: [
          { id: 1, image: 'img3.png', name: 'Pet Expo', description: 'A pet-themed fair...', date: '12/07/24', location: 'Street Park' },
          // Add other events here
        ]
      }
    }
  }
  </script>
  
  <style scoped>
  </style>
  
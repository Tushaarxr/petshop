<!-- src/components/PetList.vue -->
<template>
    <section class="bg-yellow-50 p-8">
      <div class="flex flex-row justify-between">
        <h2 class="text-2xl font-sans ml-8 text-blue-900 font-semibold text-center">Take A Look At Some Of Our Pets</h2>
        <button class="p-2 px-3 border-2 border-blue-900 font-semibold text-lg mr-12 rounded-xl text-blue-900">View More</button>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 mt-8">
        <PetCard
          v-for="pet in pets"
          :key="pet.id"
          :id="pet.id"
          :image="pet.image"
          :name="pet.name"
          :gender="pet.gender"
          :age="pet.age"
          :price="pet.price"
        />
      </div>
    </section>
  </template>
  
  <script>
  import PetCard from './PetCard.vue';
  
  export default {
    name: 'PetList',
    components: { PetCard },
    data() {
      return {
        pets: [
          { id: 1, image: "/img1.png", name: 'Pomeranian White', gender: 'Male', age: 2, price: 69000 },
          { id: 2, image: '/img2.png', name: 'Poodle Tiny Yellow', gender: 'Female', age: 2, price: 39000 },
          { id: 3, image: "/img4.png", name: 'Pomeranian White', gender: 'Male', age: 2, price: 69000 },
          { id: 4, image: '/img5.png', name: 'Poodle Tiny Yellow', gender: 'Female', age: 2, price: 39000 },
          { id: 5, image: "/img1.png", name: 'Pomeranian White', gender: 'Male', age: 2, price: 69000 },
          { id: 6, image: '/img2.png', name: 'Poodle Tiny Yellow', gender: 'Female', age: 2, price: 39000 },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  </style>
  
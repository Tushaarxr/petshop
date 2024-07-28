<!-- src/components/PetCard.vue -->
<template>
  <div class="bg-white p-4 shadow rounded-lg">
    <img :src="image" alt="pet" class="w-full h-40 object-cover rounded">
    <div>
      <h2 class="mt-2 text-xl font-bold">{{ name }}</h2>
      <p class="text-gray-600">Gender: {{ gender }}</p>
      <p class="text-gray-600">Age: {{ age }} months</p>
      <div class="flex">
        <div>
          <p class="text-blue-900 font-bold justify-start mt-3">{{ price }} INR</p>
        </div>
        <div class="justify-end ml-24">
          <button @click="navigateToDetail" class="bg-blue-900 text-white px-4 py-2 rounded">Explore</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PetCard',
  props: {
    id: Number,
    image: String,
    name: String,
    gender: String,
    age: Number,
    price: Number,
  },
  methods: {
    navigateToDetail() {
      this.$router.push({ name: 'PetDetail', params: { id: this.id } });
    },
  },
};
</script>

<style scoped>
</style>

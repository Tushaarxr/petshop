<template>
  <main class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="text-center">
      <!-- Hero Image -->
      <img
        src="https://via.placeholder.com/800x400.png?text=Welcome+to+Petify"
        alt="Welcome to Petify"
        class="mx-auto mb-8 rounded-lg shadow-lg"
      />

      <!-- Welcome Text -->
      <h1 class="text-4xl font-bold text-gray-800 mb-4">Welcome to Petify</h1>
      <p class="text-xl text-gray-600 mb-6">
        Your one-stop shop for finding the perfect furry companion. Explore our wide selection of pets and pet supplies.
      </p>

      <!-- CTA Button -->
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Explore Now
      </button>
    </div>
  </main>
</template>

<script>
export default {
  name: "WelcomePage",
};
</script>

<style scoped>
/* Add any specific styling here if needed */
</style>

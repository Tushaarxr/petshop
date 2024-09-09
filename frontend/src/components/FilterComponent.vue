<template>
  <div class="filter-component flex items-center space-x-4 p-4 bg-orange-50 rounded-lg shadow-md">
    <!-- Category Filter -->
    <div class="flex-1">
      <label class="block text-gray-700 mb-1">Category</label>
      <select v-model="filters.category" class="form-select block w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
        <option value="">All</option>
        <option v-for="category in categories" :key="category" :value="category">
          {{ category }}
        </option>
      </select>
    </div>

    <!-- Breed Filter -->
    <div class="flex-1">
      <label class="block text-gray-700 mb-1">Breed</label>
      <select v-model="filters.breed" class="form-select block w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
        <option value="">All</option>
        <option v-for="breed in breeds" :key="breed" :value="breed">
          {{ breed }}
        </option>
      </select>
    </div>

    <!-- Price Filter -->
    <div class="flex-1">
      <label class="block text-gray-700 mb-1">Price Range</label>
      <div class="flex space-x-2">
        <input
          type="number"
          v-model="filters.minPrice"
          placeholder="Min"
          class="form-input block w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          v-model="filters.maxPrice"
          placeholder="Max"
          class="form-input block w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
    </div>

    <!-- Apply Button -->
    <div class="flex-1">
      <button
        @click="applyFilters"
        class="w-full bg-blue-900 text-white font-bold px-4 py-2 rounded-md shadow hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        Apply Filters
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    categories: Array,
    breeds: Array,
  },
  data() {
    return {
      filters: {
        category: "",
        breed: "",
        minPrice: "",
        maxPrice: "",
      },
    };
  },
  methods: {
    applyFilters() {
      this.$emit("filter-ads", this.filters);
    },
  },
};
</script>

<style scoped>
.filter-component {
  max-width: 100%;
}
</style>
<!-- src/components/Adoption.vue -->
<template>
  <section class="bg-[url('/AdoptionBanner.png')] bg-cover p-24 text-center">
    <div class="flex flex-col items-start justify-center text-blue-900">
      <h2 class="text-3xl font-bold">Events</h2>
      <p class="text-xl mt-2">Find exciting and engaging new events for your pet</p>
      <p class="mt-4">
        Expolre the Event section to know more 
      </p>
      <div class="mt-6">
        <router-link to="/events">
          <button
            class="border-2 border-blue-900 text-blue-900 px-6 py-2 rounded mr-2"
          >
            Explore Events
          </button>
        </router-link>
        <router-link to="/events/create">
          <button
            class="border-2 border-blue-900 text-blue-900 px-6 py-2 rounded"
          >
            Create Event
          </button>
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Adoption",
};
</script>

<style scoped></style>

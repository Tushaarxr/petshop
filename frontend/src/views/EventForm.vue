<template>
  <div class="max-w-xl mx-auto p-6 bg-white rounded shadow-md">
    <h1 class="text-2xl font-bold mb-4">Create Event</h1>
    <form @submit.prevent="submitForm" class="space-y-4">
      <div>
        <label for="title" class="block text-sm font-medium text-gray-700">Title</label>
        <input type="text" v-model="title" id="title" class="mt-1 block w-full border border-gray-300 rounded p-2" required />
      </div>
      <div>
        <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
        <textarea v-model="description" id="description" class="mt-1 block w-full border border-gray-300 rounded p-2" required></textarea>
      </div>
      <div>
        <label for="date" class="block text-sm font-medium text-gray-700">Date</label>
        <input type="date" v-model="date" id="date" class="mt-1 block w-full border border-gray-300 rounded p-2" required />
      </div>
      <div>
        <label for="location" class="block text-sm font-medium text-gray-700">Location</label>
        <input type="text" v-model="location" id="location" class="mt-1 block w-full border border-gray-300 rounded p-2" required />
      </div>
      <div>
        <label for="image" class="block text-sm font-medium text-gray-700">Image</label>
        <input type="file" ref="file" @change="handleFileUpload" id="image" class="mt-1 block w-full text-gray-700 border border-gray-300 rounded p-2" />
      </div>
      <button type="submit" class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700">Create Event</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      title: '',
      description: '',
      date: '',
      location: '',
      image: null,  // Store the selected file here
    };
  },
  methods: {
    handleFileUpload(event) {
      this.image = event.target.files[0];
    },
    async submitForm() {
      let formData = new FormData();
      if (this.image) {
        formData.append('image', this.image);
      }
      formData.append('title', this.title);
      formData.append('description', this.description);
      formData.append('date', this.date);
      formData.append('location', this.location);

      try {
        const response = await axios.post('/api/posts/events/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('Event created:', response.data);
        this.resetForm(); // Clear form fields after successful submission
        this.$router.push('/events'); // Redirect to events list after creation
      } catch (error) {
        console.error('Error creating event:', error);
        alert('Failed to create event. Please try again.');
      }
    },
    resetForm() {
      this.title = '';
      this.description = '';
      this.date = '';
      this.location = '';
      this.image = null;
      if (this.$refs.file) {
        this.$refs.file.value = null; // Reset file input value
      }
    },
  },
};
</script>

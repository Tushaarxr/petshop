<template>
  <div class="max-w-7xl mx-auto p-8 bg-white rounded shadow-md">
    <h1 class="text-2xl font-bold mb-4">Events</h1>
    <div v-if="events.length">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
        <div v-for="event in events" :key="event.id" class="border border-gray-200 p-4 rounded-lg shadow-sm bg-white">
          <!-- Display event images if they exist -->
          <div v-if="event.attachments.length">
            <div v-for="attachment in event.attachments" :key="attachment.id" class="mb-6">
              <img :src="attachment.image_url" alt="Event Image" class="w-full h-48 object-cover rounded">
            </div>
          </div>
          <h2 class="text-xl font-semibold mb-2">{{ event.title }}</h2>
          <p class="text-gray-700 mb-2">{{ event.description }}</p>
          <p class="text-gray-500 mb-2">{{ event.date }}</p>
          <p class="text-gray-500 mb-4">{{ event.location }}</p>
          <!-- Register button for each event -->
          <button 
            @click="registerForEvent(event.id)" 
            class="bg-green-500 text-white font-bold py-2 px-4 rounded hover:bg-green-700 w-full"
          >
            Register
          </button>
        </div>
      </div>
    </div>
    <div v-else>
      <p class="text-gray-700">No events available.</p>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      events: [],
    };
  },
  created() {
    this.fetchEvents();
  },
  methods: {
    fetchEvents() {
      axios.get('/api/posts/events/')
        .then(response => {
          this.events = response.data;
        })
        .catch(error => {
          console.error('Error fetching events:', error.response.data);
        });
    },
    registerForEvent(eventId) {
      axios.post(`/api/posts/events/register/${eventId}/`)
        .then(response => {
          console.log('Registered for event:', response.data);
          alert('Successfully registered for the event!');
        })
        .catch(error => {
          console.error('Error registering for event:', error.response.data);
          alert('Failed to register for the event.');
        });
    },
  },
};
</script>

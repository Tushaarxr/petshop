<template>
  <div class="main-center col-span-2 space-y-4">
    <div class="bg-white border border-gray-200 rounded-lg shadow-md p-6">
      <form @submit.prevent="updatePost" method="post">
        <!-- Section: Basic Information -->
        <div class="mb-6">
          <h2 class="text-xl font-semibold mb-4 text-gray-700">Basic Information</h2>
          <h3>Title</h3>
          <input
            v-model="post.title"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Title (e.g., Golden Retriever Puppy for Sale)"
          />
          <h3>Description</h3>
          <textarea
            v-model="post.description"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            rows="4"
            placeholder="Description (Provide details about the pet)"
          ></textarea>
        </div>

        <!-- Section: Contact & Price -->
        <div class="mb-6">
          <h2 class="text-xl font-semibold mb-4 text-gray-700">Contact & Price</h2>
          <h3>Contact</h3>
          <input
            v-model="post.contact_information"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Contact Information (e.g., Phone, Email)"
          />
          <h3>Price</h3>
          <input
            v-model="post.price"
            type="number"
            step="0.01"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Price (in USD)"
          />
        </div>

        <!-- Section: Pet Details -->
        <div class="mb-6">
          <h2 class="text-xl font-semibold mb-4 text-gray-700">Pet Details</h2>
          <h3>Category</h3>
          <input
            v-model="post.category"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Category (e.g., Dog, Cat)"
          />
          <h3>Breed</h3>
          <input
            v-model="post.breed"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Breed (e.g., Labrador, Persian)"
          />
          <h3>Color</h3>
          <input
            v-model="post.color"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Color (e.g., Brown, White)"
          />
          <h3>Age(In Months)</h3>
          <input
            v-model="post.age"
            type="number"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Age (in months)"
          />
        </div>

        <!-- Section: Additional Information -->
        <div class="mb-6">
          <h2 class="text-xl font-semibold mb-4 text-gray-700">Additional Information</h2>
          <h3>Vaccinated</h3>
          <select v-model="post.vaccinated" class="p-4 w-full bg-gray-100 rounded-lg mb-4">
            <option value="true">Vaccinated</option>
            <option value="false">Not Vaccinated</option>
          </select>
          <h3>Gender</h3>
          <select v-model="post.gender" class="p-4 w-full bg-gray-100 rounded-lg mb-4">
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
          <h3>Weight</h3>
          <input
            v-model="post.weight"
            type="number"
            step="0.01"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Weight (in kg)"
          />
          <h3>Microchipped</h3>
          <select v-model="post.microchipped" class="p-4 w-full bg-gray-100 rounded-lg mb-4">
            <option value="true">Microchipped</option>
            <option value="false">Not Microchipped</option>
          </select>
          <h3>Training</h3>
          <select v-model="post.trained" class="p-4 w-full bg-gray-100 rounded-lg mb-4">
            <option value="true">Trained</option>
            <option value="false">Not Trained</option>
          </select>
          <h3>Health Certificate</h3>
          <select v-model="post.health_certificate" class="p-4 w-full bg-gray-100 rounded-lg mb-4">
            <option value="true">Health Certificate Available</option>
            <option value="false">No Health Certificate</option>
          </select>
          <h3>Additional Message</h3>
          <textarea
            v-model="post.body"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            rows="3"
            placeholder="Add a personal message or additional details"
          ></textarea>
        </div>

        <!-- Submit Button -->
        <div class="border-t border-gray-100 pt-4 flex justify-end">
          <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg hover:bg-purple-700">
            Update Post
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EditPost",
  data() {
    return {
      post: {
        title: "",
        description: "",
        contact_information: "",
        price: 0,
        category: "",
        breed: "",
        color: "",
        age: null,
        vaccinated: "false",
        gender: "",
        weight: null,
        microchipped: "false",
        trained: "false",
        health_certificate: "false",
        body: "",
      },
      errors: [],
    };
  },
  methods: {
   async fetchPost() {
  try {
    const response = await axios.get(`/api/posts/${this.$route.params.id}/`);
    const data = response.data.post; // Accessing the post data directly
    console.log("Fetched post data:", data); // Log fetched data

    this.post = {
      title: data.title || "",
      description: data.description || "",
      contact_information: data.contact_information || "",
      price: data.price || 0,
      category: data.category || "",
      breed: data.breed || "",
      color: data.color || "",
      age: data.age || null,
      vaccinated: data.vaccinated ? "true" : "false",
      gender: data.gender || "",
      weight: data.weight || null,
      microchipped: data.microchipped ? "true" : "false",
      trained: data.trained ? "true" : "false",
      health_certificate: data.health_certificate ? "true" : "false",
      body: data.body || "",
    };
  } catch (error) {
    console.error("Error fetching post:", error);
    alert("Error fetching post data.");
  }
}

,
    async updatePost() {
      this.errors = [];
      if (this.post.title === '') this.errors.push('Title is required');
      if (this.post.description === '') this.errors.push('Description is required');
      // Add any other validations as needed

      if (this.errors.length === 0) {
        try {
          const updatedPost = { ...this.post };

          // Convert string values back to booleans
          updatedPost.vaccinated = updatedPost.vaccinated === "true";
          updatedPost.microchipped = updatedPost.microchipped === "true";
          updatedPost.trained = updatedPost.trained === "true";
          updatedPost.health_certificate = updatedPost.health_certificate === "true";

          const response = await axios.put(`/api/posts/${this.$route.params.id}/edit/`, updatedPost);

          alert("Post updated successfully");
          this.$router.push(`/${this.$route.params.id}`);
        } catch (error) {
          console.error("Error updating post:", error.response.data);
          alert("Error updating post");
        }
      }
    },
  },
  created() {
    this.fetchPost();
  },
};
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
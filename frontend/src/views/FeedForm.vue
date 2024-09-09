<template>
  <div class="main-center col-span-2 space-y-4">
    <div
      class="bg-white border border-gray-200 rounded-lg shadow-md p-6"
     
    >
      <form v-on:submit.prevent="submitForm" method="post">
        <!-- Section: Basic Information -->
        <div class="mb-6">
          <h2 class="text-xl font-semibold mb-4 text-gray-700">
            Basic Information
          </h2>
          <input
            v-model="title"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Title (e.g., Golden Retriever Puppy for Sale)"
          />
          <textarea
            v-model="description"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            rows="4"
            placeholder="Description (Provide details about the pet)"
          ></textarea>
        </div>

        <!-- Section: Contact & Price -->
        <div class="mb-6">
          <h2 class="text-xl font-semibold mb-4 text-gray-700">
            Contact & Price
          </h2>
          <input
            v-model="contact_information"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Contact Information (e.g., Phone, Email)"
          />
          <input
            v-model="price"
            type="number"
            step="0.01"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Price (in USD)"
          />
        </div>

        <!-- Section: Pet Details -->
        <div class="mb-6">
          <h2 class="text-xl font-semibold mb-4 text-gray-700">Pet Details</h2>
          <input
            v-model="category"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Category (e.g., Dog, Cat)"
          />
          <input
            v-model="breed"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Breed (e.g., Labrador, Persian)"
          />
          <input
            v-model="color"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Color (e.g., Brown, White)"
          />
          <input
            v-model="age"
            type="number"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Age (in months)"
          />
        </div>

        <!-- Section: Additional Information -->
        <div class="mb-6">
          <h2 class="text-xl font-semibold mb-4 text-gray-700">
            Additional Information
          </h2>
          <h3>Vaccinated</h3>
          <select
            v-model="vaccinated"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
          >
            <option value="true">Vaccinated</option>
            <option value="false">Not Vaccinated</option>
          </select>
          <h3>Gender</h3>
          <select
            v-model="gender"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
          >
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
          <h3>Weight</h3>
          <input
            v-model="weight"
            type="number"
            step="0.01"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            placeholder="Weight (in kg)"
          />
          <h3>Microchipped</h3>
          <select
            v-model="microchipped"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
          >
            <option value="true">Microchipped</option>
            <option value="false">Not Microchipped</option>
          </select>
          <h3>Training</h3>
          <select
            v-model="trained"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
          >
            <option value="true">Trained</option>
            <option value="false">Not Trained</option>
          </select>
          <h3>Health Certificate</h3>
          <select
            v-model="health_certificate"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
          >
            <option value="true">Health Certificate Available</option>
            <option value="false">No Health Certificate</option>
          </select>
          <textarea
            v-model="body"
            class="p-4 w-full bg-gray-100 rounded-lg mb-4"
            rows="3"
            placeholder="Add a personal message or additional details"
          ></textarea>
        </div>

        <!-- Image Preview and Upload -->
        <div class="mb-6">
          <h2 class="text-xl font-semibold mb-4 text-gray-700">Image Upload</h2>
          <div id="preview" v-if="url" class="mb-4">
            <img
              :src="url"
              class="w-32 h-32 object-cover mt-3 rounded-lg shadow-sm"
            />
          </div>
          <label
            class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg cursor-pointer"
          >
            <input
              type="file"
              ref="file"
              @change="onFileChange"
              class="hidden"
            />
            Attach image
          </label>
        </div>

        <!-- Submit Button -->
        <div class="border-t border-gray-100 pt-4 flex justify-end">
          <button
            class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg hover:bg-purple-700"
          >
            Post
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useUserStore } from "@/stores/user";
import { useToastStore } from "@/stores/toast";


export default {
  name: "FeedForm",

  setup() {
    const userStore = useUserStore();
    const toastStore = useToastStore();

    return {
      userStore,
      toastStore,
    };
  },

  components: {
   
  },

  data() {
    return {
     
      body: "",
      url: null,
      title: "",
      description: "",
      contact_information: "",
      price: "",
      category: "",
      breed: "",
      color: "",
      age: null,
      vaccinated: "",
      gender: "",
      weight: null,
      microchipped: "",
      trained: "",
      health_certificate: "",
    };
  },

 

  

  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
    },

  

    

   

    submitForm() {
      let formData = new FormData();
      formData.append("image", this.$refs.file.files[0]);
      formData.append("body", this.body);
      formData.append("title", this.title);
      formData.append("description", this.description);
      formData.append("contact_information", this.contact_information);
      formData.append("price", this.price);
      formData.append("category", this.category);
      formData.append("breed", this.breed);
      formData.append("color", this.color);
      formData.append("age", this.age);
      formData.append("vaccinated", this.vaccinated);
      formData.append("gender", this.gender);
      formData.append("weight", this.weight);
      formData.append("microchipped", this.microchipped);
      formData.append("trained", this.trained);
      formData.append("health_certificate", this.health_certificate);

      axios
        .post("/api/posts/create/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          this.posts.unshift(response.data);
          this.body = "";
          this.title = "";
          this.description = "";
          this.contact_information = "";
          this.price = "";
          this.category = "";
          this.breed = "";
          this.color = "";
          this.age = null;
          this.vaccinated = "";
          this.gender = "";
          this.weight = null;
          this.microchipped = "";
          this.trained = "";
          this.health_certificate = "";
          this.$refs.file.value = null;
          this.url = null;
          this.user.posts_count += 1;
        })
        .catch((error) => {
          console.error("error", error);
        });
    },

  
  },
};
</script>

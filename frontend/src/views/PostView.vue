<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-center col-span-4 flex">
      <!-- Image Section -->
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg w-2/3"
        v-if="post.id"
      >
        <img
          v-for="image in post.attachments"
          v-bind:key="image.id"
          :src="image.get_image"
          alt="pet"
          class="w-full h-auto rounded-lg object-cover"
        />

        <div class="flex justify-around mt-4 text-gray-600">
          <button @click="handleLike" class="flex items-center space-x-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              class="h-6 w-6"
            >
            <path
                fill="currentColor"
                d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"
            />
            </svg>
            <span>Like</span>
          </button>

          <button @click="handleComment" class="flex items-center space-x-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              class="h-6 w-6"
            >
            <path
                fill-rule="evenodd"
                d="M12 2C6.477 2 2 6.036 2 11.059c0 2.385.957 4.637 2.642 6.284-.311 1.11-1.138 2.647-2.442 4.604-.103.168-.107.38-.01.553.096.172.281.275.48.275 3.209 0 5.678-1.27 7.33-2.397a9.863 9.863 0 0 0 1.91.186c5.523 0 10-4.036 10-9.059C22 6.036 17.523 2 12 2zm-3.25 7.5a.75.75 0 0 1 0-1.5h6.5a.75.75 0 0 1 0 1.5h-6.5zm0 4a.75.75 0 0 1 0-1.5h3.5a.75.75 0 0 1 0 1.5h-3.5z"
                clip-rule="evenodd"
              />
            </svg>
            <span>Comments</span>
          </button>

          <button @click="handleBookmark" class="flex items-center space-x-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              :fill="isBookmarked ? 'black' : 'none'"
              viewBox="0 0 24 24"
              stroke="currentColor"
              class="h-6 w-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z"
              />
            </svg>
            <span>Bookmark</span>
          </button>
        </div>
      </div>

      <!-- Title, Description, and Details Section (Outside of the white box) -->
      <div class="ml-8 flex-1 space-y-4">
        <h2 class="text-3xl font-bold">{{ post.title }}</h2>
        <p class="text-2xl text-gray-800">{{ post.price }} USD</p>

        <!-- Additional Details -->
        <div class="space-y-2">
          <div v-for="(value, label) in petDetails" :key="label" class="flex justify-between">
            <span class="font-bold">{{ label }}:</span>
            <span>{{ value }}</span>
          </div>
        </div>

        <!-- Description -->
        <div class="mb-2">
          <p class="font-bold">Description:</p>
          <p class="text-gray-700">{{ post.description }}</p>
        </div>

        <!-- Contact Details -->
        <div class="mb-2">
          <p class="font-bold">Contact Details:</p>
          <p class="text-gray-700">Mobile Number: {{ post.contact_information }}</p>
        </div>

        <!-- Other Information -->
        <div class="mb-2">
           <p class="font-bold">Category:</p>
           <p class="text-gray-700">{{ post.category }}</p>
        </div>

        <div class="mb-2">
           <p class="font-bold">Breed:</p>
           <p class="text-gray-700">{{ post.breed }}</p>
        </div>

        <div class="mb-2">
           <p class="font-bold">Colour:</p>
           <p class="text-gray-700">{{ post.color }}</p>
        </div>

        <div class="mb-2">
           <p class="font-bold">Age:</p>
           <p class="text-gray-700">{{ post.age }}</p>
        </div>

        <div class="mb-2">
           <p class="font-bold">Vaccinated:</p>
           <p class="text-gray-700">{{ post.vaccinated }}</p>
        </div>

        <div class="mb-2">
           <p class="font-bold">Gender:</p>
           <p class="text-gray-700">{{ post.gender }}</p>
        </div>

        <div class="mb-2">
           <p class="font-bold">Weight:</p>
           <p class="text-gray-700">{{ post.weight }}</p>
        </div>

        <div class="mb-2">
           <p class="font-bold">Microchipped:</p>
           <p class="text-gray-700">{{ post.microchipped }}</p>
        </div>

        <div class="mb-2">
           <p class="font-bold">Trained:</p>
           <p class="text-gray-700">{{ post.trained }}</p>
        </div>

        <div class="mb-2">
           <p class="font-bold">Health certificate:</p>
           <p class="text-gray-700">{{ post.health_certificate }}</p>
        </div>
      </div>
    </div>

    <!-- Comment Section -->
    <div class="col-span-4 space-y-4">
      <button
        class="py-2 px-4 bg-purple-600 text-sm text-white rounded-lg"
        @click="sendDirectMessage"
      >
        Send direct message
      </button>

      <!-- Comments -->
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg"
        v-for="comment in post.comments"
        v-bind:key="comment.id"
      >
        <CommentItem v-bind:comment="comment" />
      </div>

      <!-- Add New Comment -->
      <div class="bg-white border border-gray-200 rounded-lg">
        <form v-on:submit.prevent="submitForm" method="post">
          <div class="p-4">
            <textarea
              v-model="body"
              class="p-4 w-full bg-gray-100 rounded-lg"
              placeholder="What do you think?"
            ></textarea>
          </div>

          <div class="p-4 border-t border-gray-100">
            <button
              class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
            >
              Comment
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

import CommentItem from "../components/CommentItem.vue";
import FeedDetail from "../components/FeedDetail.vue";
import { useUserStore } from "@/stores/user";
import { useToastStore } from "@/stores/toast";

export default {
  name: "PostView",

  setup() {
    const userStore = useUserStore();
    const toastStore = useToastStore();

    return {
      userStore,
      toastStore,
    };
  },

  components: {
    CommentItem,
    FeedDetail,
  },

  data() {
    return {
      post: {
        id: null,
        comments: [],
        postCreatorId: null, // Store post creator's ID here
        body: "",
      },
      body: "",
    };
  },

  mounted() {
    this.getPost();
  },

  methods: {
    getPost() {
      axios
        .get(`/api/posts/${this.$route.params.id}/`)
        .then((response) => {
          this.post = response.data.post;
          this.postCreatorId = response.data.user.id;
        })
        .catch((error) => {
          console.error(
            "Error fetching post:",
            error.response ? error.response.data : error.message
          );
        });
    },

    sendDirectMessage() {
      // Use the post creator's user ID instead of the post ID
      axios
        .get(`/api/chat/${this.post.created_by.id}/get-or-create/`) // Pass creator's user ID
        .then((response) => {
          this.$router.push("/chat");
        })
        .catch((error) => {
          console.error("Error creating chat:", error);
        });
    },

    submitForm() {
      axios
        .post(`/api/posts/${this.$route.params.id}/comment/`, {
          body: this.body,
        })
        .then((response) => {
          this.post.comments.push(response.data);
          this.body = "";
        })
        .catch((error) => {
          console.error(
            "Error submitting comment:",
            error.response ? error.response.data : error.message
          );
        });
    },
  },
};
</script>
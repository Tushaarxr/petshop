<template>
  <div
    class="mb-10 flex items-center justify-between bg-white p-4 shadow rounded-lg"
  >
    <div class="flex items-center space-x-6">
      <img :src="post.created_by.get_avatar" class="w-[30px] rounded-full" />

      <p>
        <strong>
          <RouterLink
            :to="{ name: 'profile', params: { id: post.created_by.id } }"
            >{{ post.created_by.name }}</RouterLink
          >
        </strong>
      </p>
    </div>

    <p class="text-gray-600">{{ post.created_at_formatted }} ago</p>
  </div>

  <div class="flex justify my-10">
    <template
      v-if="post.attachments.length"
      class="max-w-40 h-40 object-cover rounded"
    >
      <img
        v-for="image in post.attachments"
        v-bind:key="image.id"
        :src="image.get_image"
        class="max-w-100 h-100 ml-20 mr-20 object-cover rounded"
      />
    </template>
    <div class="bg-white p-4    rounded-lg">
      <p class="text-gray-600"><strong>Title:</strong> {{ post.title }}</p>
      <p class="text-gray-600">
        <strong>Description:</strong> {{ post.description }}
      </p>
      <p class="text-gray-600">
        <strong>Contact Information:</strong> {{ post.contact_information }}
      </p>
      <p class="text-gray-600"><strong>Price:</strong> {{ post.price }}</p>
      <p class="text-gray-600">
        <strong>Category:</strong> {{ post.category }}
      </p>
      <p class="text-gray-600"><strong>Breed:</strong> {{ post.breed }}</p>
      <p class="text-gray-600"><strong>Color:</strong> {{ post.color }}</p>
      <p class="text-gray-600"><strong>Age:</strong> {{ post.age }}</p>
      <p class="text-gray-600">
        <strong>Vaccinated:</strong> {{ post.vaccinated }}
      </p>
      <p class="text-gray-600"><strong>Gender:</strong> {{ post.gender }}</p>
      <p class="text-gray-600"><strong>Weight:</strong> {{ post.weight }}</p>
      <p class="text-gray-600">
        <strong>Microchipped:</strong> {{ post.microchipped }}
      </p>
      <p class="text-gray-600"><strong>Trained:</strong> {{ post.trained }}</p>
      <p class="text-gray-600">
        <strong>Health Certificate:</strong> {{ post.health_certificate }}
      </p>
    </div>
  </div>

  <p>{{ post.body }}</p>

  <div class="my-6 flex justify-between">
    <div class="flex space-x-6 items-center">
      <div class="flex items-center space-x-2" @click="likePost(post.id)">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
          ></path>
        </svg>

        <span class="text-gray-500 text-xs">{{ post.likes_count }} likes</span>
      </div>

      <div class="flex items-center space-x-2">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"
          ></path>
        </svg>

        <RouterLink
          :to="{ name: 'postview', params: { id: post.id } }"
          class="text-gray-500 text-xs"
          >{{ post.comments_count }} comments</RouterLink
        >
      </div>
    </div>

    <div>
      <div @click="toggleExtraModal">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"
          ></path>
        </svg>
      </div>
    </div>
  </div>

  <div class="flex space-x-6 items-center">
    <div
      class="flex items-center space-x-2"
      @click="deletePost"
      v-if="userStore.user.id == post.created_by.id"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-6 h-6 text-red-500"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0"
        />
      </svg>

      <span class="text-red-500 text-xs">Delete post</span>
    </div>

    <!-- Bookmark Icon -->
    <div class="flex items-center space-x-2" @click="bookmarkPost(post.id)">
      <svg
        v-if="post.is_bookmarked"
        xmlns="http://www.w3.org/2000/svg"
        fill="currentColor"
        viewBox="0 0 24 24"
        class="w-6 h-6 text-yellow-500"
      >
        <path d="M6 4v16l6-5.333L18 20V4z" />
      </svg>
      <svg
        v-else
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        class="w-6 h-6"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M5 5l7-3 7 3v16l-7-3-7 3V5z"
        />
      </svg>

      <span class="text-gray-500 text-xs">{{
        post.is_bookmarked ? "Bookmarked" : "Bookmark"
      }}</span>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { RouterLink } from "vue-router";
import { useUserStore } from "@/stores/user";
import { useToastStore } from "@/stores/toast";

export default {
  props: {
    post: Object,
  },

  emits: ["deletePost"],

  setup() {
    const userStore = useUserStore();
    const toastStore = useToastStore();

    return {
      userStore,
      toastStore,
    };
  },

  data() {
    return {
      showExtraModal: false,
    };
  },

  methods: {
    likePost(id) {
      axios
        .post(`/api/posts/${id}/like/`)
        .then((response) => {
          if (response.data.message == "like created") {
            this.post.likes_count += 1;
          }
        })
        .catch((error) => {
          console.log("error", error);
        });
    },

    bookmarkPost(id) {
      axios
        .post(`/api/posts/${id}/bookmark/`)
        .then((response) => {
          if (response.data.message == "bookmark created") {
            this.post.is_bookmarked = true;
          } else if (response.data.message == "bookmark removed") {
            this.post.is_bookmarked = false;
          }
        })
        .catch((error) => {
          console.log("error", error);
        });
    },

    reportPost() {
      axios
        .post(`/api/posts/${this.post.id}/report/`)
        .then((response) => {
          console.log(response.data);

          this.toastStore.showToast(
            5000,
            "The post was reported",
            "bg-emerald-500"
          );
        })
        .catch((error) => {
          console.log("error", error);
        });
    },

    deletePost() {
      this.$emit("deletePost", this.post.id);

      axios
        .delete(`/api/posts/${this.post.id}/delete/`)
        .then((response) => {
          console.log(response.data);

          this.toastStore.showToast(
            5000,
            "The post was deleted",
            "bg-emerald-500"
          );
        })
        .catch((error) => {
          console.log("error", error);
        });
    },

    toggleExtraModal() {
      console.log("toggleExtraModal");

      this.showExtraModal = !this.showExtraModal;
    },
  },
  components: { RouterLink },
};
</script>

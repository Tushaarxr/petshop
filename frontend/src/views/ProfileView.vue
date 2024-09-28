<template>
  <div
    class="max-w-7xl mx-auto p-6 mb-6 mt-4 bg-white border border-gray-200 rounded-lg"
  >
    <div class="flex items-start space-x-6">
      <!-- User Avatar and Info -->
      <div class="flex-shrink-0">
        <img :src="user.get_avatar" class="w-32 h-32 rounded-full" />
      </div>
      <div class="flex-1">
        <p class="text-xl font-semibold mb-2">
          <strong>{{ user.name }}</strong>
        </p>
        <div class="flex space-x-10 mb-10" v-if="user.id">
          <RouterLink
            :to="{ name: 'friends', params: { id: user.id } }"
            class="text-sm text-gray-500"
            >{{ user.friends_count }} Buddies</RouterLink
          >
          <p class="text-sm text-gray-500">{{ user.posts_count }} posts</p>
        </div>

        <div class="flex space-x-4">
          <button
            class="py-2 px-4 bg-purple-600 text-sm text-white rounded-lg"
            @click="sendFriendshipRequest"
            v-if="userStore.user.id !== user.id"
          >
            Send Buddy request
          </button>

          <button
            class="py-2 px-4 bg-purple-600 text-sm text-white rounded-lg"
            @click="sendDirectMessage"
            v-if="userStore.user.id !== user.id"
          >
            Send direct message
          </button>

          <RouterLink
            class="py-2 px-4 bg-purple-600 text-sm text-white rounded-lg"
            to="/profile/edit"
            v-if="userStore.user.id === user.id"
          >
            Edit profile
          </RouterLink>

          <button
            class="py-2 px-4 bg-red-600 text-sm text-white rounded-lg"
            @click="logout"
            v-if="userStore.user.id === user.id"
          >
            Log out
          </button>

          <RouterLink
            to="/feedform"
            class="py-2 px-4 bg-green-500 text-sm text-white rounded-lg"
          >
            Create Ad
          </RouterLink>
        </div>
      </div>
    </div>
  </div>

  <div class="max-w-9xl mx-auto p-6 mb-10 bg-white rounded shadow-md">
    <h1 class="text-2xl font-bold mb-4">Posts</h1>
    <div v-if="posts.length">
      <table class="min-w-full bg-white border border-gray-200 rounded-lg">
        <thead>
          <tr class="w-full bg-gray-100 border-b border-gray-200">
            <th class="px-6 py-3 text-left text-gray-600 font-medium">S.NO</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">Ad Id</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">Image</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">Title</th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Description
            </th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Published
            </th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Interests
            </th>
            <th class="px-6 py-3 text-left text-gray-600 font-medium">
              Actions
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(post, index) in posts"
            :key="post.id"
            class="border-b border-gray-200"
          >
            <td class="px-6 py-4 text-gray-500">{{ index + 1 }}</td>
            <td class="px-6 py-4 text-gray-800">{{ post.id.slice(-4) }}</td>
            <td class="px-5 py-4 text-gray-500">
              <div class="flex flex-wrap gap-2">
                <router-link
                  v-for="image in post.attachments"
                  :key="image.id"
                  :to="`/${post.id}/`"
                  class="block"
                >
                  <img
                    :src="image.get_image"
                    class="w-32 h-32 object-cover rounded-lg cursor-pointer"
                  />
                </router-link>
              </div>
            </td>

            <td class="px-6 py-4 text-gray-800">{{ post.title }}</td>
            <td class="px-6 py-4 text-gray-600">{{ post.description }}</td>
            <td class="px-6 py-4 text-gray-500">
              {{ post.created_at_formatted }} Ago
            </td>
            <td class="px-6 py-4 text-gray-500">
              {{ post.likes_count }} Likes, {{ post.comments_count }} Comments
            </td>
            <td class="px-6 py-4 text-gray-500">
              <div class="flex items-center space-x-2">
                <button
                  @click="editPost(post.id)"
                  class="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-600"
                  v-if="userStore.user.id === post.created_by.id"
                >
                  Edit
                </button>
                <button
                  @click="deletePost(post.id)"
                  class="bg-red-500 text-white font-bold py-2 px-4 rounded hover:bg-red-600"
                  v-if="userStore.user.id === post.created_by.id"
                >
                  Delete
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
      <p class="text-gray-700">No posts available.</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import FeedItem from "../components/FeedItem.vue";
import { useUserStore } from "@/stores/user";
import { useToastStore } from "@/stores/toast";
import { RouterLink } from "vue-router";
import FeedForm from "./FeedForm.vue";

export default {
  name: "FeedView",

  setup() {
    const userStore = useUserStore();
    const toastStore = useToastStore();

    return {
      userStore,
      toastStore,
    };
  },

  components: {
    FeedItem,
    FeedForm,
  },

  data() {
    return {
      posts: [],
      user: {
        id: "",
      },
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

  mounted() {
    this.getFeed();
  },

  watch: {
    "$route.params.id": {
      handler: function () {
        this.getFeed();
      },
      deep: true,
      immediate: true,
    },
  },

  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
    },

    sendDirectMessage() {
      axios
        .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
        .then((response) => {
          this.$router.push("/chat");
        })
        .catch((error) => {
          console.error("error", error);
        });
    },

    sendFriendshipRequest() {
      axios
        .post(`/api/friends/${this.$route.params.id}/request/`)
        .then((response) => {
          if (response.data.message == "request already sent") {
            this.toastStore.showToast(
              5000,
              "The request has already been sent!",
              "bg-red-300"
            );
          } else {
            this.toastStore.showToast(
              5000,
              "The request was sent!",
              "bg-emerald-300"
            );
          }
        })
        .catch((error) => {
          console.error("error", error);
        });
    },

    getFeed() {
      axios
        .get(`/api/posts/profile/${this.$route.params.id}/`)
        .then((response) => {
          this.posts = response.data.posts;
          this.user = response.data.user;

          this.user.posts_count = this.posts.length;
        })
        .catch((error) => {
          console.error("error", error);
        });
    },

    deletePost(postId) {
      this.$emit("deletePost", postId);

      axios
        .delete(`/api/posts/${postId}/delete/`)
        .then((response) => {
          console.log(response.data);

          // Refresh the feed
          this.getFeed();

          // Show a toast message
          this.toastStore.showToast(5000, "The post was deleted", "bg-red-500");

          // Refresh the profile page
          window.location.reload(); // This will refresh the current page to reflect changes
        })
        .catch((error) => {
          console.log("error", error);
        });
    },

    editPost(postId) {
      console.log("Redirecting to edit page for post ID:", postId);
      this.$router.push(`/${postId}/edit/`).catch((err) => {
        console.error("Navigation error:", err);
      });
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

    logout() {
      this.userStore.removeToken();
      this.$router.push("/login");
    },
  },
};
</script>

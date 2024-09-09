<template>
  <header
    class="px-8 py-4 flex justify-between items-center bg-orange-100 z-10"
  >
    <!-- Logo and Brand Name -->
    <div class="text-3xl text-blue-900 font-bold">Petify</div>

    <!-- Navigation Links -->
    <nav v-if="userStore.user.isAuthenticated" class="flex space-x-12">
      <RouterLink to="/feed" class="hover:text-blue-900">
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
            d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
          />
        </svg>
      </RouterLink>

      <RouterLink to="/chat" class="hover:text-blue-900">
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
            d="M8.625 9.75a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 01.778-.332 48.294 48.294 0 005.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z"
          ></path>
        </svg>
      </RouterLink>

      <RouterLink to="/notifications" class="hover:text-blue-900">
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
            d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0"
          ></path>
        </svg>
      </RouterLink>

      <RouterLink to="/search" class="hover:text-blue-900">
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
            d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
          ></path>
        </svg>
      </RouterLink>

      <RouterLink to="/bookmarks" class="hover:text-blue-900">
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
            d="M17.25 3.75H6.75A2.25 2.25 0 004.5 6v13.439a.75.75 0 001.133.653l6.367-3.536a.75.75 0 01.7 0l6.367 3.536a.75.75 0 001.133-.653V6a2.25 2.25 0 00-2.25-2.25z"
          ></path>
        </svg>
      </RouterLink>
    </nav>

    <!-- Login/Sign Up or User Avatar -->
    <div class="flex items-center space-x-4">
      <template v-if="userStore.user.isAuthenticated && userStore.user.id">
        <RouterLink
          :to="{ name: 'profile', params: { id: userStore.user.id } }"
        >
          <img :src="userStore.user.avatar" class="w-12 rounded-full" />
        </RouterLink>
      </template>

      <template v-else>
        <RouterLink to="/login">
          <button
            class="border-2 bg-blue-900 text-white px-6 py-2 rounded-3xl mr-2"
          >
            Login
          </button>
        </RouterLink>
        <RouterLink to="/signup">
          <button class="bg-blue-900 text-white px-6 py-2 rounded-3xl">
            Sign Up
          </button>
        </RouterLink>
      </template>
    </div>
  </header>

  <main class="bg-gray-100 flex flex-col min-h-screen">
    <RouterView class="flex-1" />
    <Footer></Footer>
  </main>

  <Toast />
</template>

<script>
import axios from "axios";
import Toast from "@/components/Toast.vue";
import { useUserStore } from "@/stores/user";
import Footer from "./components/Footer.vue";

export default {
  setup() {
    const userStore = useUserStore();

    return {
      userStore,
    };
  },

  components: {
    Toast,
    Footer,
  },

  beforeCreate() {
    this.userStore.initStore();

    const token = this.userStore.user.access;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
};
</script>

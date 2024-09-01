<!-- src/components/PetCard.vue -->
<template>
  <div class="bg-white p-4 shadow rounded-lg">
    <div> 
      <img :src="image" alt="pet" class="w-full h-40 object-cover rounded">
    </div>
    
    <div>
      <h2 class="mt-2 text-xl font-bold">{{ name }}</h2>
      <p class="text-gray-600">Gender: {{ gender }}</p>
      <p class="text-gray-600">Age: {{ age }} months</p>
      <div class="flex">
        <div>
          <p class="text-blue-900 font-bold justify-start mt-3">{{ price }} INR</p>
        </div>
        <div class="justify-end ml-24">
          <button @click="navigateToDetail" class="bg-blue-900 text-white px-4 py-2 rounded">Explore</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    props: {
        post: Object
    },

    emits: ['deletePost'],

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    data() {
        return {
            showExtraModal: false
        }
    },

    methods: {
        likePost(id) {
            axios
                .post(`/api/posts/${id}/like/`)
                .then(response => {
                    if (response.data.message == "like created") {
                        this.post.likes_count += 1;
                    }
                })
                .catch(error => {
                    console.log("error", error);
                });
        },

        bookmarkPost(id) {
            axios
                .post(`/api/posts/${id}/bookmark/`)
                .then(response => {
                    if (response.data.message == "bookmark created") {
                        this.post.is_bookmarked = true;
                    } else if (response.data.message == "bookmark removed") {
                        this.post.is_bookmarked = false;
                    }
                })
                .catch(error => {
                    console.log("error", error);
                });
        },

        reportPost() {
            axios
                .post(`/api/posts/${this.post.id}/report/`)
                .then(response => {
                    console.log(response.data)

                    this.toastStore.showToast(5000, 'The post was reported', 'bg-emerald-500')
                })
                .catch(error => {
                    console.log("error", error);
                })
        },

        deletePost() {
            this.$emit('deletePost', this.post.id)

            axios
                .delete(`/api/posts/${this.post.id}/delete/`)
                .then(response => {
                    console.log(response.data)

                    this.toastStore.showToast(5000, 'The post was deleted', 'bg-emerald-500')
                })
                .catch(error => {
                    console.log("error", error);
                })
        },

        toggleExtraModal() {
            console.log('toggleExtraModal')

            this.showExtraModal = !this.showExtraModal
        }
    },
    components: { RouterLink }
}
</script>
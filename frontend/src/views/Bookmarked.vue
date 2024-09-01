<template>
    <div class="p-4">
        <h2 class="text-2xl mb-4">Your Bookmarked Posts</h2>
        <div v-if="bookmarkedPosts.length">
            <div v-for="post in bookmarkedPosts" :key="post.id" class="mb-4 p-4 bg-white rounded-lg shadow">
                <RouterLink :to="{ name: 'postview', params: { id: post.id } }">
                    <h3 class="text-xl">{{ post.title }}</h3>
                </RouterLink>
                <p>{{ post.description }}</p>
            </div>
        </div>
        <div v-else>
            <p>You haven't bookmarked any posts yet.</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { RouterLink } from 'vue-router'

export default {
    data() {
        return {
            bookmarkedPosts: []
        }
    },

    created() {
        this.fetchBookmarkedPosts();
    },

    methods: {
        fetchBookmarkedPosts() {
            axios
                .get('/api/posts/bookmarks/')
                .then(response => {
                    this.bookmarkedPosts = response.data;
                })
                .catch(error => {
                    console.log("error", error);
                });
        }
    },

    components: { RouterLink }
}
</script>

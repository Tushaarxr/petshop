<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <img :src="user.get_avatar" class="mb-6 rounded-full">
                
                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around" v-if="user.id">
                    <RouterLink :to="{name: 'friends', params: {id: user.id}}" class="text-xs text-gray-500">{{ user.friends_count }} Buddies</RouterLink>
                    <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p>
                </div>

                <div class="mt-6">
                    <button 
                        class="inline-block py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                        @click="sendFriendshipRequest"
                        v-if="userStore.user.id !== user.id"
                    >
                        Send Buddy request
                    </button>

                    <button 
                        class="inline-block mt-4 py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                        @click="sendDirectMessage"
                        v-if="userStore.user.id !== user.id"
                    >
                        Send direct message
                    </button>

                    <RouterLink 
                        class="inline-block mr-2 py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" 
                        to="/profile/edit"
                        v-if="userStore.user.id === user.id"
                    >
                        Edit profile
                    </RouterLink>

                    <button 
                        class="inline-block py-4 px-3 bg-red-600 text-xs text-white rounded-lg" 
                        @click="logout"
                        v-if="userStore.user.id === user.id"
                    >
                        Log out
                    </button>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
         
            <div 
                class="bg-white border border-gray-200 rounded-lg"
                v-if="userStore.user.id === user.id"
            >
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4">  
                        <input v-model="title" class="p-4 w-full bg-gray-100 rounded-lg mb-2" placeholder="Title">
                        <textarea v-model="description" class="p-4 w-full bg-gray-100 rounded-lg mb-2" placeholder="Description"></textarea>
                        <input v-model="contact_information" class="p-4 w-full bg-gray-100 rounded-lg mb-2" placeholder="Contact Information">
                        <input v-model="price" type="number" step="0.01" class="p-4 w-full bg-gray-100 rounded-lg mb-2" placeholder="Price">
                        <input v-model="category" class="p-4 w-full bg-gray-100 rounded-lg mb-2" placeholder="Category">
                        <input v-model="breed" class="p-4 w-full bg-gray-100 rounded-lg mb-2" placeholder="Breed">
                        <input v-model="color" class="p-4 w-full bg-gray-100 rounded-lg mb-2" placeholder="Color">
                        <input v-model="age" type="number" class="p-4 w-full bg-gray-100 rounded-lg mb-2" placeholder="Age (in months)">
                        <select v-model="vaccinated" class="p-4 w-full bg-gray-100 rounded-lg mb-2">
                            <option value="true">Vaccinated</option>
                            <option value="false">Not Vaccinated</option>
                        </select>
                        <select v-model="gender" class="p-4 w-full bg-gray-100 rounded-lg mb-2">
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                        </select>
                        <input v-model="weight" type="number" step="0.01" class="p-4 w-full bg-gray-100 rounded-lg mb-2" placeholder="Weight (in kg)">
                        <select v-model="microchipped" class="p-4 w-full bg-gray-100 rounded-lg mb-2">
                            <option value="true">Microchipped</option>
                            <option value="false">Not Microchipped</option>
                        </select>
                        <select v-model="trained" class="p-4 w-full bg-gray-100 rounded-lg mb-2">
                            <option value="true">Trained</option>
                            <option value="false">Not Trained</option>
                        </select>
                        <select v-model="health_certificate" class="p-4 w-full bg-gray-100 rounded-lg mb-2">
                            <option value="true">Health Certificate Available</option>
                            <option value="false">No Health Certificate</option>
                        </select>

                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg mb-2" placeholder="Add Message"></textarea>

                        <div id="preview" v-if="url">
                            <img :src="url" class="w-[100px] mt-3 rounded-xl" />
                        </div>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <label class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">
                            <input type="file" ref="file" @change="onFileChange">
                            Attach image
                        </label>

                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="post in posts"
                v-bind:key="post.id"
            >
                <FeedItem v-bind:post="post" />
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />

            <Trends />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'
import { RouterLink } from 'vue-router'

export default {
    name: 'FeedView',

    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore
        }
    },

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem
    },

    data() {
        return {
            posts: [],
            user: {
                id: ''
            },
            body: '',
            url: null,
            title: '',
            description: '',
            contact_information: '',
            price: '',
            category: '',
            breed: '',
            color: '',
            age: null,
            vaccinated: '',
            gender: '',
            weight: null,
            microchipped: '',
            trained: '',
            health_certificate: ''
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: { 
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
        onFileChange(e) {
            const file = e.target.files[0];
            this.url = URL.createObjectURL(file);
        },

        sendDirectMessage() {
            axios
                .get(`/api/chat/${this.$route.params.id}/get-or-create/`)
                .then(response => {
                    this.$router.push('/chat')
                })
                .catch(error => {
                    console.error('error', error)
                })
        },

        sendFriendshipRequest() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`)
                .then(response => {
                    if (response.data.message == 'request already sent') {
                        this.toastStore.showToast(5000, 'The request has already been sent!', 'bg-red-300')
                    } else {
                        this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-300')
                    }
                })
                .catch(error => {
                    console.error('error', error)
                })
        },

        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    this.posts = response.data.posts
                    this.user = response.data.user
                })
                .catch(error => {
                    console.error('error', error)
                })
        },

        submitForm() {
            let formData = new FormData()
            formData.append('image', this.$refs.file.files[0])
            formData.append('body', this.body)
            formData.append('title', this.title)
            formData.append('description', this.description)
            formData.append('contact_information', this.contact_information)
            formData.append('price', this.price)
            formData.append('category', this.category)
            formData.append('breed', this.breed)
            formData.append('color', this.color)
            formData.append('age', this.age)
            formData.append('vaccinated', this.vaccinated)
            formData.append('gender', this.gender)
            formData.append('weight', this.weight)
            formData.append('microchipped', this.microchipped)
            formData.append('trained', this.trained)
            formData.append('health_certificate', this.health_certificate)

            axios
                .post('/api/posts/create/', formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    }
                })
                .then(response => {
                    this.posts.unshift(response.data)
                    this.body = ''
                    this.title = ''
                    this.description = ''
                    this.contact_information = ''
                    this.price = ''
                    this.category = ''
                    this.breed = ''
                    this.color = ''
                    this.age = null
                    this.vaccinated = ''
                    this.gender = ''
                    this.weight = null
                    this.microchipped = ''
                    this.trained = ''
                    this.health_certificate = ''
                    this.$refs.file.value = null
                    this.url = null
                    this.user.posts_count += 1
                })
                .catch(error => {
                    console.error('error', error)
                })
        },

        logout() {
            this.userStore.removeToken()
            this.$router.push('/login')
        }
    }
}
</script>

<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-center col-span-3 space-y-4">
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg"
        v-if="post.id"
      >
        <FeedDetail v-bind:post="post" />
      </div>

      <div>
        <button
          class="py-2 px-4 bg-purple-600 text-sm text-white rounded-lg"
          @click="sendDirectMessage"
          
        >
          Send direct message
        </button>
      </div>

      <div
        class="p-4 ml-6 bg-white border border-gray-200 rounded-lg"
        v-for="comment in post.comments"
        v-bind:key="comment.id"
      >
        <CommentItem v-bind:comment="comment" />
      </div>

 

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

<!-- 
   <template>
    <div>
      <Header />
      <div class="flex bg-orange-50 justify-center p-8">
        <div class="bg-white rounded-lg shadow-lg p-8 max-w-4xl w-full">
          <div class="flex flex-col md:flex-row" >
            <div  v-if="post.attachments.length">
                <img v-for="image in post.attachments" v-bind:key="image.id" :src="image.get_image" alt="pet" class="w-full md:w-1/2 rounded-lg mb-4 md:mb-0 object-cover">

            </div>
           
            <div class="md:ml-8 flex-1">
              <div class="flex flex-col items-start mb-6">
                <span class="text-gray-600">SKU #{{ post.id}}</span>
                <h2 class="text-3xl font-bold mb-2">{{ post.title }}</h2>
                <p class="text-2xl text-gray-800 mb-4">{{ post.price }} INR</p>
                <button class="bg-blue-500 text-white rounded-md py-2 px-4 hover:bg-blue-600 transition">Save</button>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                <div v-for="(value, label) in petDetails" :key="label" class="flex justify-between">
                  <span class="font-bold">{{ label }}:</span>
                  <span>{{ value }}</span>
                </div>
              </div>
              <div class="mb-6">
                <p class="font-bold">Additional Information:</p>
                <p class="text-gray-700">{{ post.description }}</p>
              </div>
              <div class="mb-6">
                <p class="font-bold">Contact Details:</p>
                <p class="text-gray-700">Mobile Number: {{ post.contact_information}}</p>
                
              </div>
              <div class="flex space-x-4">
                <a href="#" class="text-blue-500 hover:text-blue-600"><i class="fab fa-facebook"></i></a>
                <a href="#" class="text-blue-500 hover:text-blue-600"><i class="fab fa-twitter"></i></a>
                <a href="#" class="text-blue-500 hover:text-blue-600"><i class="fab fa-instagram"></i></a>
                <a href="#" class="text-blue-500 hover:text-blue-600"><i class="fab fa-youtube"></i></a>
              </div>
            </div>
          </div>
  
          
          <div v-if="post.id" class="mt-8">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
              <FeedItem :post="post" />
            </div>
  
            <div v-for="comment in post.comments" :key="comment.id" class="p-4 ml-6 bg-white border border-gray-200 rounded-lg mt-4">
              <CommentItem :comment="comment" />
            </div>
          </div>
  
          
          <div class="bg-white border border-gray-200 rounded-lg mt-8">
            <form @submit.prevent="submitForm" method="post">
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
      <Footer />
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
        getPost() {
        axios
          .get(`/api/posts/${this.$route.params.id}/`)
          .then((response) => {
            this.post = response.data.post
          })
          .catch((error) => {
            console.error(
              'Error fetching post:',
              error.response ? error.response.data : error.message
            )
          })
      },





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
</script> -->

<template>
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-4  py-12 p-12 bg border border-custom-border rounded-lg shadow-lg">
      <div class="main-left flex flex-col justify-center">
        
          <h1 class="mb-6 text-3xl font-bold text-custom-dark">Log in</h1>
          <p class="mb-6 text-custom-medium">
            <!-- Additional text can go here -->
          </p>
          <p class="font-bold text-custom-dark">
            Don't have an account? 
            <RouterLink :to="{name: 'signup'}" class="underline italic hover:not-italic text-custom-accent">Click here</RouterLink> 
            to create one!
          </p>
       
      </div>
  
      <div class="main-right flex flex-col justify-center">
        <div class="p-12 bg-custom-light border border-custom-border rounded-lg shadow-lg">
          <form class="space-y-6" v-on:submit.prevent="submitForm">
            <div>
              <label class="block text-custom-dark font-bold">E-mail</label>
              <input type="email" v-model="form.email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-custom-border rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-accent">
            </div>
            <div>
              <label class="block text-custom-dark font-bold">Password</label>
              <input type="password" v-model="form.password" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-custom-border rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-accent">
            </div>
            <template v-if="errors.length > 0">
              <div class="bg-custom-error text-white rounded-lg p-6">
                <p v-for="error in errors" :key="error">{{ error }}</p>
              </div>
            </template>
            <div>
              <button class="w-full py-4 px-6 bg-custom-accent text-white rounded-lg font-bold font-bold transition ease-in-out delay-150 bg-custom-accent hover:-translate-y-1 hover:scale-110 bg-custom-accent-dark:hover duration-300">Log in</button>
            </div>
          </form>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.password === '') {
                this.errors.push('Your password is missing')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/login/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        console.log('error', error)

                        this.errors.push('The email or password is incorrect! Or the user is not activated!')
                    })
            }
            
            if (this.errors.length === 0) {
                await axios
                    .get('/api/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data)

                        this.$router.push('/feed')
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>

<style scoped>
.bg-custom-light {
  background-color: #F1DEC6;
}
.bg{
    background-color: #FFF8E8;
}
.bg-custom-error {
  background-color: #C6A969;
}
.border-custom-border {
  border-color: #E59BE9;
}
.text-custom-dark {
  color: #8644A2;
}
.text-custom-accent {
  color: #8644A2;
}
.bg-custom-accent {
  background-color: #8644A2;
}
.bg-custom-accent-dark:hover {
  background-color: #6d3784; /* Darker shade of #8644A2 */
}
</style>

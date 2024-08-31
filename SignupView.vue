<template>
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-4 py-10 px-10 bg border border-custom-border rounded-lg shadow-lg">
      <!-- Left Section with Sign Up Information -->
      <div class="main-left flex flex-col justify-center">
        <h1 class="mb-6 text-3xl font-bold text-custom-dark">Sign up</h1>
        <p class="font-bold text-custom-dark">
          Already have an account? 
          <RouterLink :to="{ name: 'login' }" class="underline italic hover:not-italic text-custom-accent">Click here</RouterLink> 
          to log in!
        </p>
      </div>
      
      <!-- Right Section with Form -->
      <div class="main-right flex flex-col justify-center">
        <div class="p-10 bg-custom-light border border-custom-border rounded-lg shadow-lg">
          <form class="space-y-4" v-on:submit.prevent="submitForm">
            <div>
              <label class="block text-custom-dark font-bold">Name</label>
              <input 
                type="text" 
                v-model="form.name" 
                placeholder="Your full name" 
                class="w-full mt-2 py-4 px-4 border border-custom-border rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-accent">
            </div>
            <div>
              <label class="block text-custom-dark font-bold">E-mail</label>
              <input 
                type="email" 
                v-model="form.email" 
                placeholder="Your e-mail address" 
                class="w-full mt-2 py-4 px-4 border border-custom-border rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-accent">
            </div>
            <div>
              <label class="block text-custom-dark font-bold">Password</label>
              <input 
                type="password" 
                v-model="form.password1" 
                placeholder="Your password" 
                class="w-full mt-2 py-4 px-4 border border-custom-border rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-accent">
            </div>
            <div>
              <label class="block text-custom-dark font-bold">Repeat password</label>
              <input 
                type="password" 
                v-model="form.password2" 
                placeholder="Repeat your password" 
                class="w-full mt-2 py-4 px-4 border border-custom-border rounded-lg focus:outline-none focus:ring-2 focus:ring-custom-accent">
            </div>
            <template v-if="errors.length > 0">
              <div class="bg-custom-error text-white rounded-lg p-4">
                <p v-for="error in errors" :key="error">{{ error }}</p>
              </div>
            </template>
            <div>
              <button 
                class="w-full py-3 px-4 bg-custom-accent text-white rounded-lg font-bold transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 bg-custom-accent-dark:hover duration-300">Sign up
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </template>

<script>
import axios from 'axios'

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered. Please activate your account by clicking your email link.', 'bg-emerald-500')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }

                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
                        }
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

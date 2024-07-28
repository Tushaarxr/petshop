<!-- src/components/PetDetail.vue -->
<template>
    <div class="max-w-6xl mx-auto p-6 bg-white shadow-md rounded-lg">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="flex flex-col items-center">
          <img :src="pet.image" alt="Pet Image" class="w-full rounded-lg">
          <div class="mt-4">
            <h3 class="text-xl font-bold">Contact Details:</h3>
            <p class="mt-2">Mobile Number: <a href="tel:98475983875" class="text-blue-600">98475983875</a></p>
            <p>Email: <a href="mailto:petify123@gmail.com" class="text-blue-600">petify123@gmail.com</a></p>
            <div class="flex space-x-4 mt-4">
              <a href="#" class="text-gray-500"><i class="fab fa-facebook"></i></a>
              <a href="#" class="text-gray-500"><i class="fab fa-twitter"></i></a>
              <a href="#" class="text-gray-500"><i class="fab fa-instagram"></i></a>
              <a href="#" class="text-gray-500"><i class="fab fa-youtube"></i></a>
            </div>
          </div>
        </div>
        <div>
          <h2 class="text-2xl font-bold">{{ pet.name }}</h2>
          <p class="text-xl text-blue-600">{{ pet.price }} VND</p>
          <button class="mt-4 bg-blue-600 text-white py-2 px-4 rounded-lg">Save</button>
          <div class="mt-6 grid grid-cols-1 gap-2">
            <div class="grid grid-cols-2">
              <span class="font-bold">SKU:</span>
              <span>#{{ pet.sku }}</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Gender:</span>
              <span>{{ pet.gender }}</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Age:</span>
              <span>{{ pet.age }} Months</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Size:</span>
              <span>{{ pet.size }}</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Color:</span>
              <span>{{ pet.color }}</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Vaccinated:</span>
              <span>{{ pet.vaccinated ? 'Yes' : 'No' }}</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Dewormed:</span>
              <span>{{ pet.dewormed ? 'Yes' : 'No' }}</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Cert:</span>
              <span>{{ pet.cert }}</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Microchip:</span>
              <span>{{ pet.microchip ? 'Yes' : 'No' }}</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Location:</span>
              <span>{{ pet.location }}</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Published Date:</span>
              <span>{{ pet.publishedDate }}</span>
            </div>
            <div class="grid grid-cols-2">
              <span class="font-bold">Additional Information:</span>
              <span>{{ pet.additionalInfo }}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="mt-8">
        <h3 class="text-xl font-bold mb-4">See More Puppies</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
          <div v-for="puppy in puppies" :key="puppy.id" class="bg-white p-4 rounded-lg shadow-md">
            <img :src="puppy.image" alt="Puppy Image" class="w-full h-32 object-cover rounded-lg">
            <h4 class="mt-4 text-lg font-bold">{{ puppy.name }}</h4>
            <p>Gender: {{ puppy.gender }}</p>
            <p>Age: {{ puppy.age }} months</p>
            <p class="mt-2 text-blue-600 font-bold">{{ puppy.price }} VND</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PetDetail',
    data() {
      return {
        pet: {
          image: require('/img1.png'), // Update the image path as per your project structure
          name: 'Shiba Inu Sepia',
          price: '34.000.000',
          sku: '1000078',
          gender: 'Female',
          age: 2,
          size: 'Small',
          color: 'Apricot & Tan',
          vaccinated: true,
          dewormed: true,
          cert: 'Yes (MKA)',
          microchip: true,
          location: 'Vietnam',
          publishedDate: '12-Oct-2022',
          additionalInfo: 'Pure breed Shih Tzu. Good body structure. With MKA cert and Microchip. Father from champion lineage.'
        },
        puppies: [
          {
            id: 1,
            image: require('../assets/puppy1.jpg'), // Update the image path as per your project structure
            name: 'Pomeranian White',
            gender: 'Male',
            age: 2,
            price: '6.900.000'
          },
          {
            id: 2,
            image: require('../assets/puppy2.jpg'), // Update the image path as per your project structure
            name: 'Poodle Tiny Yellow',
            gender: 'Female',
            age: 2,
            price: '3.900.000'
          },
          // Add more puppies here
        ]
      }
    }
  }
  </script>
  
  <style scoped>
  </style>
  
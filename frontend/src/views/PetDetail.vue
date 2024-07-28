<!-- src/views/PetDetail.vue -->
<template>
  <div>
  <Header />
  <div class="flex bg-orange-50 justify-center p-8">
    <div class="bg-white rounded-lg shadow-lg p-8 max-w-4xl w-full">
      <div class="flex flex-col md:flex-row">
        <img :src="pet.image" alt="pet" class="w-full md:w-1/2 rounded-lg mb-4 md:mb-0 object-cover">
        <div class="md:ml-8 flex-1">
          <div class="flex flex-col items-start mb-6">
            <span class="text-gray-600">SKU #{{ pet.id }}</span>
            <h2 class="text-3xl font-bold mb-2">{{ pet.name }}</h2>
            <p class="text-2xl text-gray-800 mb-4">{{ pet.price }} INR</p>
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
            <p class="text-gray-700">{{ pet.additionalInfo }}</p>
          </div>
          <div class="mb-6">
            <p class="font-bold">Contact Details:</p>
            <p class="text-gray-700">Mobile Number: {{ pet.contact.mobile }}</p>
            <p class="text-gray-700">Email: {{ pet.contact.email }}</p>
          </div>
          <div class="flex space-x-4">
            <a href="#" class="text-blue-500 hover:text-blue-600"><i class="fab fa-facebook"></i></a>
            <a href="#" class="text-blue-500 hover:text-blue-600"><i class="fab fa-twitter"></i></a>
            <a href="#" class="text-blue-500 hover:text-blue-600"><i class="fab fa-instagram"></i></a>
            <a href="#" class="text-blue-500 hover:text-blue-600"><i class="fab fa-youtube"></i></a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Footer />
</div>
</template>

<script>
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';

export default {
  name: 'PetDetail',
  components: {
      Header,
      Footer,
    },
  data() {
    return {
      pet: {
        id: '1000078',
        image: '/img1.png',
        name: 'Pomeranian White',
        price: '39000',
        gender: 'Female',
        age: '2 Months',
        size: 'Small',
        color: 'Apricot & Tan',
        vaccinated: 'Yes',
        dewormed: 'Yes',
        cert: 'Yes (MKA)',
        microchip: 'Yes',
        location: 'Vietnam',
        publishedDate: '12-Oct-2022',
        additionalInfo: 'Pure breed Shih Tzu. Good body structure. With MKA cert and Microchip. Father from champion lineage.',
        contact: {
          mobile: '98475983875',
          email: 'petify123@gmail.com',
        },
      },
    };
  },
  computed: {
    petDetails() {
      return {
        Gender: this.pet.gender,
        Age: this.pet.age,
        Size: this.pet.size,
        Color: this.pet.color,
        Vaccinated: this.pet.vaccinated,
        Dewormed: this.pet.dewormed,
        Cert: this.pet.cert,
        Microchip: this.pet.microchip,
        Location: this.pet.location,
        'Published Date': this.pet.publishedDate,
      };
    },
  },
};
</script>

<style scoped>
/* No additional styles are needed as Tailwind CSS is used */
</style>

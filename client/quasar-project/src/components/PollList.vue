<!-- src/components/PollList.vue -->

<template>
    <div class="q-pa-md">
      <h2 class="text-h6">Список голосований</h2>
      <q-list>
        <q-item v-for="poll in polls" :key="poll.id">
          <q-item-label>{{ poll.question }}</q-item-label>
        </q-item>
      </q-list>
  
      <q-btn to="/add-poll" label="Добавить голосование" color="primary" />
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  const polls = ref([]);
  
  const fetchPolls = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/polls/');
      polls.value = response.data;
    } catch (error) {
      console.error('Ошибка при загрузке голосований', error);
    }
  };
  
  onMounted(() => {
    fetchPolls();
  });
  </script>
  
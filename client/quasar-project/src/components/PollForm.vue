<!-- src/components/PollAddForm.vue -->

<template>
    <div class="q-pa-md">
      <h2 class="text-h6">Добавить голосование</h2>
      <q-form @submit.prevent="addPoll">
        <q-input v-model="question" label="Вопрос" outlined />
        <q-input v-model="options" label="Варианты ответов (через запятую)" outlined />
        <q-btn type="submit" label="Добавить" />
      </q-form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  
  const question = ref('');
  const options = ref('');
  
  const addPoll = async () => {
    try {
      const response = await axios.post('http://localhost:8000/api/polls/', {
        question: question.value,
        options: options.value.split(',').map(option => option.trim())
      });
  
      // Обновление списка голосований
      fetchPolls();
  
      // Сброс полей формы
      question.value = '';
      options.value = '';
  
      console.log('Голосование успешно добавлено:', response.data);
    } catch (error) {
      console.error('Ошибка при добавлении голосования', error);
    }
  };
  </script>
  
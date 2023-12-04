<template>
<div>
    <h2>Авторизация</h2>
    <form @submit.prevent="login">
    <label for="username">Имя пользователя:</label>
    <input v-model="username" type="text" id="username" required>
    <br>
    <label for="password">Пароль:</label>
    <input v-model="password" type="password" id="password" required>
    <br>
    <button type="submit">Войти</button>
    </form>
</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios'

const username = ref('');
const password = ref('');

const login = async () => {
try {
    const response = await axios.post('/api/login', {
    username: username.value,
    password: password.value
    });

    // Обработка успешной авторизации
    console.log('Успешная авторизация', response.data);

    // Дополнительные действия после успешной авторизации

} catch (error) {
    // Обработка ошибок авторизации
    console.error('Ошибка авторизации', error);
}
};
</script>

<style scoped>
/* Ваши стили здесь */
</style>

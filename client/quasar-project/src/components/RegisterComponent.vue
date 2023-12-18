<template>
  <div class="registration-form q-pa-md">
    <q-card>
      <q-card-section>
        <q-h2 class="text-h6">Регистрация</q-h2>
        <q-form @submit.prevent="registerUser">
          <q-input
            v-model="username"
            label="Username"
            outlined
            dense
            class="q-mb-md"
            required
          />
          <q-input
            v-model="password"
            label="Пароль"
            type="password"
            outlined
            dense
            class="q-mb-md"
            required
          />
          <q-btn
            type="submit"
            color="primary"
            label="Зарегистрироваться"
            dense
            class="q-mt-md"
          />
        </q-form>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    registerUser() {
      const userData = {
        username: this.username,
        password: this.password,
      };

      axios.post('http://localhost:8000/api/register/', userData)
        .then(response => {
          const token = response.data.token;
          localStorage.setItem('token', token);
          // Перенаправление пользователя или выполнение других действий
        })
        .catch(error => {
          console.error('Registration error:', error);
        });
    },
  },
};
</script>

<style scoped>
.registration-form {
  max-width: 400px;
  margin: 0 auto;
}
</style>

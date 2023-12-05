<template>
  <div class="q-form-container">
    <q-form @submit="submitForm">
      <q-input v-model="questionText" label="Question Text" class="q-input-label"/>
      <q-input v-model="selectedChoices" label="Select Choices (comma-separated)" class="q-input-label"/>
      <q-btn type="submit" label="Submit" class="q-btn-submit" />
    </q-form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      questionText: '',
      selectedChoices: '', // Updated to handle multiple choices separated by a comma
    };
  },
  methods: {
    submitForm() {
      // Convert comma-separated choices to an array
      const choicesArray = this.selectedChoices.split(',').map(choice => choice.trim());

      // Send form data to the server using API
      const formData = {
        questionText: this.questionText,
        selectedChoices: choicesArray,
      };

      // Call your API endpoint to create a new vote
      axios.post('http://127.0.0.1:8000/api/questions/', formData)
        .then(response => {
          // Handle successful response
          console.log('Question created successfully:', response.data);
        })
        .catch(error => {
          // Handle error
          console.error('Error creating question:', error);
        });
    }
  }
};
</script>

<style lang="scss">
.q-form-container {
  max-width: 400px;
  margin: 0 auto;
}

.q-input-label {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 8px;
}

.q-btn-submit {
  margin-top: 16px;
}

.q-field__native:focus {
  border-color: #00bcd4;
  box-shadow: 0 0 0 2px #00bcd4;
}
</style>

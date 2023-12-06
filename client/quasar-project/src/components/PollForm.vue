<template>
  <div class="q-form-container">
    <q-form @submit="submitForm">
      <q-input v-model="questionText" label="Вопрос" class="q-input-label"/>
      <q-input v-model="selectedChoices" label="Ответы (через запятую)" class="q-input-label"/>
      <q-btn type="submit" label="Submit" class="q-btn-submit" />
    </q-form>

    <q-list v-for="question in questions.question" :key="question.id" class="question-list">
      <q-item>
        <q-item-section>
          <q-item-label class="question-title">{{ question.question_text }}</q-item-label>
        </q-item-section>
        <q-item-section class="choices-section" clickable>
          <q-list v-for="choice in questions.choise" :key="choice.id" >
            <q-item v-if="question.id === choice.question" clickable @click="handleChoiceClick(choice.id)"
              :class="{ 'selected-choice': isSelectedChoice(choice.id) }">
              <q-item-section>
                <q-item-label class="choice-label">{{ choice.choice_text }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-item-section>
      </q-item>
      <q-item>
        <q-item-section side>
          <q-btn icon="delete" color="negative" flat round dense @click="deleteClick(question.id)"/>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      questionText: '',
      selectedChoices: '',
      questions: {},
      choices: [],
      selectedChoiceId: null
    };
  },
  computed: {
    questionsWithChoices() {
      return this.questions && this.questions.length ? this.questions.filter(question => question.choises.length > 0) : [];
    },
  },
  methods: {
    submitForm() {
      const choicesArray = this.selectedChoices.split(',').map(choice => choice.trim());
      const formData = {
        questionText: this.questionText,
        selectedChoices: choicesArray,
      };

      axios.post('http://127.0.0.1:8000/api/questions/', formData)
        .then(response => {
          console.log('Question created successfully:', response.data);
          this.fetchQuestions();
        })
        .catch(error => {
          console.error('Error creating question:', error);
        });
    },
    fetchQuestions() {
      axios.get('http://127.0.0.1:8000/api/card/')
        .then(response => {
          this.questions = response.data;
          this.choices = response.data['choises']
          console.log(response.data)
        })
        .catch(error => {
          console.error('Error fetching questions:', error);
        });
    },
    deleteClick(questionId) {
      axios.delete(`http://127.0.0.1:8000/api/card/${questionId}/`)
        .then(response => {
          console.log('Question deleted successfully:', response.data);
          this.fetchQuestions();
        })
        .catch(error => {
          console.error('Error deleting question:', error);
        });
    },
    handleChoiceClick(choiceId) {
      axios.post('http://127.0.0.1:8000/api/vote/', {
        'id': choiceId
      })
        .then(response => {
          console.log('Question created successfully:', response.data);
          this.fetchQuestions();
          this.selectedChoiceId = choiceId;

        })
        .catch(error => {
          console.error('Error creating question:', error);
        });
    },
    isSelectedChoice(choiceId) {
      return this.selectedChoiceId === choiceId;
    },
  },
  mounted() {
    this.fetchQuestions();
  },
};
</script>

<style lang="scss">
.q-form-container {
  max-width: 600px;
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

.question-list {
  margin-top: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.question-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.choices-section {
  margin-top: 10px;
}

.choice-list {
  margin-top: 8px;
  border: 1px solid #eee;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.choice-label {
  font-size: 16px;
}
</style>

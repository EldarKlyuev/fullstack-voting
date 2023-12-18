<template>
  <div class="q-form-container">
    <q-btn @click="logoutUser" label="Выход" color="negative" icon="logout"/>
    <q-card class="q-my-md">
      <q-card-section>
        <q-form @submit="submitForm" v-if="userRole !== 'User'">
          <q-input v-model="questionText" label="Вопрос" class="q-input-label"/>
          <q-input v-model="selectedChoices" label="Ответы (через запятую)" class="q-input-label"/>
          <q-btn type="submit" label="Сохранить" class="q-btn-submit" color="primary"/>
        </q-form>
      </q-card-section>
    </q-card>

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
                <q-item-label class="choice-label">{{ staticClickData[choice.id] || choice.choice_text }}</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-item-section>
      </q-item>
      <q-item>
        <q-item-section side>
          <q-btn icon="delete" color="negative" flat round dense @click="deleteClick(question.id)"/>
        </q-item-section>
        <q-item-section side v-if="userRole !== 'User'">
          <q-btn icon="analytics" color="primary" flat round dense @click="staticClick(question.id)"/>
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
      selectedChoiceId: null,
      userRole: '',
      staticClickData: {},
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
    staticClick(questionId) {
      axios.get(`http://127.0.0.1:8000/api/static/${questionId}/`)
        .then(response => {
          console.log(response.data)
          this.staticClickData = response.data;
          console.log(this.staticClickData);
        })
        .catch(error => {
          console.error('Error fetching static data:', error);
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
    checkRole() {
      const token = localStorage.getItem('token')

      axios.post('http://127.0.0.1:8000/api/checkrole/', {
        'token': token
      }).then(response => {
        this.userRole = response.data['role']
        console.log(this.userRole)
      })
    },
    logoutUser() {
      const token = localStorage.getItem('token')

      axios.delete('http://127.0.0.1:8000/api/logout/', {
        'token': token
      }).then(() => {
        this.$router.push('/login')
      })
    }
  },
  mounted() {
    this.fetchQuestions();
    this.checkRole();
  },
};
</script>

<style lang="scss">
$q-form-container-max-width: 600px;
$q-form-container-margin: 0 auto;

.q-form-container {
  max-width: $q-form-container-max-width;
  margin: $q-form-container-margin;
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

.selected-choice {
  border: 2px solid #209e00;
  border-radius: 8px;
  background-color: #ffffff;
}

</style>

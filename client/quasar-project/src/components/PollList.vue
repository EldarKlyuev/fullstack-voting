<template>
  <div>
    <q-list>
      <q-item v-for="vote in votes" :key="vote.id">
        <q-item-section>
          <q-item-label>{{ vote.questionText }}</q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-btn @click="voteDetails(vote.id)" label="Details" />
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script>
export default {
  data() {
    return {
      votes: [] // Populate this array with votes from the server
    };
  },
  methods: {
    voteDetails(voteId) {
      // Navigate to the details page or show a modal with details
      // Example: this.$router.push(`/votes/${voteId}`)
    }
  },
  created() {
    // Fetch the list of votes from the server
    // Example: this.$axios.get('/api/votes/').then(response => this.votes = response.data)
  }
};
</script>
